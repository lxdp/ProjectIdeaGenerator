from typing import Dict, Any, List

from psycopg2.extensions import connection, cursor

from src.queries.general import RETRIEVE_REQUESTED_EVIDENCE

class FetchSavedEvidence:

    def __init__(self,
        id: int, db_conn: connection, db_curs: cursor):
        """Initialisation method for FetchSavedEvidence.

        Args:
            id (int): ID for the requested database row.
            db_conn (connection): Represents the active connection from the
                python app the PostgresSQL server.
            db_curs (cursor): Runs the SQL queries.
        """

        self.id = id
        self.db_conn = db_conn
        self.db_curs = db_curs
    
    def run(self) -> List[Dict[str, Any]]:
        """Main orchestration workflow method for FetchSavedEvidence.

        Returns:
            List[Dict[str, Any]]: Evidence from the requested database row.
        """

        self.db_curs.execute(RETRIEVE_REQUESTED_EVIDENCE, (self.id,))
        evidence = self.db_curs.fetchone()

        return evidence[0] if evidence else []