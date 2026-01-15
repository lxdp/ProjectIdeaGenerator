from typing import List, Tuple, Dict, Any

from psycopg2.extensions import connection, cursor

from src.schemas.retrieved_saved_data import SavedData
from src.schemas.base import Parameters
from src.schemas.project_gen import ProjectList, ProjectIdeaEvidence
from src.queries.general import RETRIEVE_REQUESTED_DATA

class FetchRequestedData:

    def __init__(self,
        id: int, db_conn: connection, db_curs: cursor):
        """Initialisation method for FetchRequestedData.

        Args:
            id (int): ID for the requested database row.
            db_conn (connection): Represents the active connection from the
                python app the PostgresSQL server.
            db_curs (cursor): Runs the SQL queries.
        """

        self.id = id
        self.db_conn = db_conn
        self.db_curs = db_curs
    
    def run(self) -> Dict[str, Any]:
        """Main orchestration workflow method for FetchRequestedData.

        Returns:
            Dict[str, Any]: Holds requested database data.
        """

        requested_data = self.retrieve_requested_data()
        parsed_requested_data = self.parse_requested_data(requested_data)

        return parsed_requested_data
    
    def retrieve_requested_data(self) -> List[Tuple]:
        """Retrieves the requested data from the database.

        Returns:
            List[Tuple]: Retrieved requested data from the database.
        """

        self.db_curs.execute(RETRIEVE_REQUESTED_DATA, (self.id,))
        requested_data = self.db_curs.fetchall()

        return requested_data
    
    def parse_requested_data(self, 
        requested_data: List[Tuple]) -> Dict[str, Any]:
        """Parses the requested data from the database.
        
        Args:
            requested_data (List[Tuple]): Requested data from the database.

        Returns:
            Dict[str, Any]: Holds requested database data.
        """

        data = requested_data[0]
        relevant_data = {
            "id": data[0],
            "title": data[2],
            "parameters": data[3],
            "project_list": data[4],
            "evidence":data[5]
        }

        return relevant_data


    
