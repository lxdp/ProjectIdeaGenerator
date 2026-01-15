from typing import List, Tuple, Optional

from psycopg2.extensions import connection, cursor

from src.queries.general import RETRIEVE_DATA
from src.schemas.retrieved_saved_data import SavedData, SavedDataList
from src.schemas.base import Parameters
from src.schemas.project_gen import ProjectList, ProjectIdeaEvidence

class FetchSavedData:

    def __init__(self, db_conn: connection, db_curs: cursor):
        self.db_conn = db_conn
        self.db_curs = db_curs


    def run(self) -> Optional[SavedDataList]:
        """Main orchestration workflow method.

        Returns:
            Optional[SavedDataList]: Contains the saved data from the PostgreSQL
                database, or None if the database is empty.
        """

        retrieved_data = self.retrieve_data()
        parsed_data = self.parse_retrieved_data(retrieved_data)

        return parsed_data

    def retrieve_data(self) -> List[Tuple]:
        """Retrieves data from the history database.

        Returns:
            List[Tuple]: Retrieved data from the database.
        """

        self.db_curs.execute(RETRIEVE_DATA)
        data = self.db_curs.fetchall()

        return data
    
    def parse_retrieved_data(self,
        retrieved_data: List[Tuple]) -> SavedDataList:
        """Parses the retrieved database data.

        Args:
            retrieved_data (List[Tuple]): Retrieved data from the
                database.
        
        Returns:
            SavedDataList: Schema for the parsed data from the database.
        """

        saved_data_list = []
        for row in retrieved_data:
            relevant_data = {
                "id": row[0],
                "title": row[2],
                "parameters": row[3],
                "project_list": row[4],
                "evidence":row[5]
            }
            saved_data_list.append(SavedData(**relevant_data))
        
        return SavedDataList(root=saved_data_list)
