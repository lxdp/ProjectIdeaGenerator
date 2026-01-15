import os
from typing import List, Dict, Any

from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

from src.schemas.project_gen import (
    JobHighlights, 
    ProjectIdeaEvidence, 
    UxInformation, 
    JobInformation, 
    PromptData,
    ProjectList
)
from src.prompts.project_gen import PROJECT_GEN_PROMPT

class ProjectGenApi():

    def __init__(self, job_listings: List[Dict[str, Any]]):
        """Initialisation method for ProjectGenApi.

        Args:
            job_listings (List[Dict[str, Any]]): Retrieved job listings based
                off user input filters.
        """

        self.job_listings = job_listings

        self.client = AzureOpenAI(
            api_key = os.getenv("AZURE_OPENAI_KEY"),
            azure_endpoint = os.getenv("AZURE_ENDPOINT"),
            api_version = os.getenv("API_VERSION")
        )
    
    def run(self) -> UxInformation:
        """Main orchestration workflow method for ProjectGenApi.

        Returns:
            UxInformation: Schema containing generated project list and evidence 
                that the project listings meet job listing qualifications.
        """

        evidence_list = []
        prompt_data_list = []
        for response in self.job_listings["job_listings"]:
            for job in response:
                evidence = self.parse_evidence(job)
                p_data = self.parse_prompt_data(job)

                evidence_list.append(evidence)
                prompt_data_list.append(p_data)
        
        project_evidence = ProjectIdeaEvidence(root=evidence_list)
        prompt_data = PromptData(root=prompt_data_list)

        project_list = self.generate_project_list(prompt_data)

        ux_information = {
            "parameters": self.job_listings["parameters"],
            "project_list": project_list,
            "evidence": project_evidence
        }

        return UxInformation(**ux_information)

    def parse_evidence(self, job: Dict[str, Any]) -> JobInformation:
        """Parses the job listing information as evidence for the project list.

        Args:
            job (Dict[str, Any]): Contains job listing information.

        Returns:
            JobInformation: Schema to hold the job listing data.
        """

        highlights = job.get("job_highlights")
        job_information = {
            "job_id": job.get("job_id"),
            "job_title": job.get("job_title"),
            "employer_name": job.get("employer_name"),
            "job_location": job.get("job_location"),
            "job_is_remote": job.get("job_is_remote"),
            "job_employment_type": job.get("job_employment_type"),
            "job_posted_at": job.get("job_posted_at"),
            "job_apply_link": job.get("job_apply_link"),
            "job_publisher": job.get("job_publisher"),
            "Qualifications": highlights.get("Qualifications")
        }

        return JobInformation(**job_information)
    
    def parse_prompt_data(self, job: Dict[str, Any]) -> JobHighlights:
        """Parses prompt data for the GPT model.

        Args:
            job (Dict[str, Any]): Contains job listing information.

        Returns:
            PromptData: Schema to hold the prompt data.
        """

        highlights = job.get("job_highlights")
        prompt_data = {
            "Qualifications": highlights.get("Qualifications"),
            "job_description": job.get("job_description")
        }

        return JobHighlights(**prompt_data)
    
    def generate_project_list(self, prompt_data: PromptData) -> ProjectList:
        """Uses GPT model to generate a project list.

        Args:
            prompt_data (PromptData): Prompt data to aid the prompting of the
                GPT model.
        """

        prompt = PROJECT_GEN_PROMPT.format(data=prompt_data)
        response = self.client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                    {
                        "role": "system", 
                        "content": "Generate a list of projects"
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                response_format=ProjectList
        )
        
        return response.choices[0].message.parsed


        

