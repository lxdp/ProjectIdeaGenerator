from typing import Dict, Any, List, Optional

from psycopg2.extensions import connection, cursor

from src.pipelines.job_listings_api import JobListingsApi
from src.pipelines.project_generation_api import ProjectGenApi
from src.pipelines.project_evidence import ProjectEvidence
from src.pipelines.save_project_data import SaveProjectData
from src.pipelines.fetch_saved_data import FetchSavedData
from src.pipelines.fetch_requested_data import FetchRequestedData
from src.pipelines.fetch_saved_evidence import FetchSavedEvidence
from src.schemas.jsearch_user_view import UserJobSearchResponses
from src.schemas.project_gen import UxInformation
from src.schemas.project_evidence import ProjectListRelevance
from src.schemas.retrieved_saved_data import SavedDataList

class MainPipeline():

    def job_search(self, user_inputs: Dict[str, Any]) -> UserJobSearchResponses:
        """Triggers the JobListingApi pipeline.

        Args:
            user_inputs (Dict[str, Any]): Holds the user parameters for job
                search filters.
        
        Returns:
            UserJobSearchResponses: A schema that contains a list of job
                listings and parameters.
        """

        jl_api = JobListingsApi(**user_inputs)
        job_listings = jl_api.run()

        return job_listings
    
    def project_idea_generation(self, 
        job_listings: List[Dict[str, Any]]) -> UxInformation:
        """Triggers the ProjectGenApi pipeline.

        Args:
            job_listings (List[Dict[str, Any]]): Holds the retrieved job
                listings based of the user input filters.

        Returns:
            UxInformation: Contains project list and evidence for the
                project list.
        """

        project_gen_api = ProjectGenApi(job_listings)
        project_gen_data = project_gen_api.run()
    
        return project_gen_data
    
    def parse_evidence(self,
        ux_info: Dict[str, Any]) -> ProjectListRelevance:
        """Triggers the ProjectEvidence pipeline.

        Args:
            ux_info (Dict[str, Any]): Carries the project lists and evidence
                for the project list relevance to the job market.
        
        Returns:
            ProjectListRelevance: Schema to carry the list of project names and
                the job role requirements that they achieve.
        """

        project_evidence = ProjectEvidence(ux_info)
        project_list_evidence = project_evidence.run()

        return project_list_evidence
    
    def save_project_data(self,
        ux_info: Dict[str, Any],
        parsed_evidence: List[Dict[str, Any]],
        db_conn: connection, 
        db_curs: cursor
    ):
        """Triggers the SaveProjectData pipeline.

        Args:
            ux_info (Dict[str, Any]): Carries the project lists and evidence
                for the project list relevance to the job market.
            parsed_evidence (List[Dict[str, Any]]): Carries list of project 
                names and the job role requirements that they achieve.
            db_conn (connection): Represents the active connection from the
                python app the PostgresSQL server.
            db_curs (cursor): Runs the SQL queries.
        """

        save_project = SaveProjectData(
            ux_info,
            parsed_evidence,
            db_conn, 
            db_curs
        )
        save_project.run()

    def fetch_saved_data(self,
        db_conn: connection, db_curs: cursor) -> Optional[SavedDataList]:
        """Triggers the FetchSavedData pipeline.

        Args:
            db_conn (connection): Represents the active connection from the
                python app the PostgresSQL server.
            db_curs (cursor): Runs the SQL queries.

        Returns:
            Optional[SavedDataList]: Contains the saved data from the PostgreSQL
                database, or None if the database is empty.
        """

        saved_data = FetchSavedData(db_conn, db_curs)
        retrieved_data = saved_data.run()

        return retrieved_data
    
    def fetch_requested_data(self,
        id: int, db_conn: connection, db_curs: cursor) -> Dict[str, Any]:
        """Retrieves requested saved data from the database.

        Args:
            id (int): ID for the requested database row.
            db_conn (connection): Represents the active connection from the
                python app the PostgresSQL server.
            db_curs (cursor): Runs the SQL queries.
        
        Returns:
            Dict[str, Any]: Holds requested database data.
        """

        fetch_requested_data = FetchRequestedData(id, db_conn, db_curs)
        requested_data = fetch_requested_data.run()

        return requested_data
    
    def fetch_saved_evidence(self,
        id: int, db_conn: connection, db_curs: cursor) -> List[Dict[str, Any]]:
        """Retrieves requested saved evidence from the database.

        Args:
            id (int): ID for the requested database row.
            db_conn (connection): Represents the active connection from the
                python app the PostgresSQL server.
            db_curs (cursor): Runs the SQL queries.
        
        Returns:
            List[Dict[str, Any]]: Holds requested database data.
        """

        fetch_evidence = FetchSavedEvidence(id, db_conn, db_curs)
        evidence = fetch_evidence.run()

        return evidence



