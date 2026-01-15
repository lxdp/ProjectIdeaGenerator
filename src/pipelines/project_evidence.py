import os
from typing import Dict, Any, List

from thefuzz import fuzz
from dotenv import load_dotenv

load_dotenv()

from src.schemas.project_evidence import (
    ProjectListRelevance,
    Match
)
from src.utils.text_normalisation import text_normalisation

class ProjectEvidence():

    def __init__(self, ux_info: Dict[str, Any]):
        """Initalisation method for ProjectEvidence.

        Args:
            ux_info (Dict[str, Any]): Carries the project lists and evidence
                for the project list relevance to the job market.
        """

        self.ux_info = ux_info
    
    def run(self) -> ProjectListRelevance:
        """Main orchestration workflow method for ProjectEvidence.

        Returns:
            ProjectListRelevance: Schema to carry the list of project names and
                the job role requirements that they achieve.
        """

        all_matches = []
        print(self.ux_info)
        for project in self.ux_info["project_list"]["projects"]:
            for j_listing in self.ux_info["evidence"]:
                matches = self.parse_project_evidence(project, j_listing)
                all_matches.extend(matches)
        
        return ProjectListRelevance(root=all_matches)

    def parse_project_evidence(self, 
        project: Dict[str, Any], evidence: Dict[str, Any]) -> List[Match]:
        """Parses the real-world job market relavance of a project.

        Args:
            project (Dict[str, Any]): A project from the list of generated
                projects.
            evidence (Dict[str, Any]): Job listing information.
        
        Returns:
            List[Match]: List of matches between project achievements
                and job qualifications.
        """

        achieved_qualifications = project["achieved_qualifications"]
        job_qualifications = evidence.get("Qualifications") or []

        matches = []
        for proj_q in achieved_qualifications:
            for job_q in job_qualifications:
                overlap = self.calc_token_overlap(proj_q, job_q)
                fuzz_sim = self.calc_fuzzy_similarity(proj_q, job_q)

                final_sim = 0.4 * overlap + 0.6 * fuzz_sim

                if final_sim >= 0.40:
                    match = Match(
                        project_title = project["title"],
                        project_achievement=proj_q,
                        job_title=evidence["job_title"],
                        company_name=evidence["employer_name"],
                        qualification=job_q
                    )
                    matches.append(match)
        
        return matches
    
    def calc_token_overlap(self, 
        achievement: str, job_qualification: str) -> float:
        """Calculates Jaccard similarity between normalised strings.

        Args:
            achievement (str): Contains an achievement that the project
                carries out.
            job_qualification (str): Contains a job qualification.
        
        Returns:
            float: Returns a float value between 0 and 1.
        """

        norm_achieve = text_normalisation(achievement)
        norm_qual = text_normalisation(job_qualification)

        return len(norm_achieve & norm_qual) / len(norm_achieve | norm_qual)
    
    def calc_fuzzy_similarity(self,
        achievement: str, job_qualification: str) -> float:
        """Calculates fuzzy string similarity.

        Args:
            achievement (str): Contains an achievement that the project
                carries out.
            job_qualification (str): Contains a job qualification.
        
        Returns:
            float: Returns a float value between 0 and 1.
        """

        sim = fuzz.token_set_ratio(achievement, job_qualification)
        return sim / 100

    
