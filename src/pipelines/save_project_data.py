import json
from typing import Dict, Any, List, Optional
from datetime import datetime

from src.queries.general import ADD_HISTORY

from psycopg2.extensions import connection, cursor

class SaveProjectData:

    def __init__(self, 
        ux_info: Dict[str, Any],
        parsed_evidence: List[Dict[str, Any]],
        db_conn: connection, 
        db_curs: cursor
    ):
        """Initialisation method for SaveProjectData.

        Args:
            ux_info (Dict[str, Any]): Carries the project lists and evidence
                for the project list relevance to the job market.
            parsed_evidence (List[Dict[str, Any]]): Carries list of project 
                names and the job role requirements that they achieve.
            db_conn (connection): Represents the active connection from the
                python app the PostgresSQL server.
            db_curs (cursor): Runs the SQL queries.
        """

        self.ux_info = ux_info
        self.parsed_evidence = parsed_evidence
        self.db_conn = db_conn
        self.db_curs = db_curs

    def run(self):
        """Main orchestration workflow method.

        """

        parameters = self.ux_info["parameters"]
        queries = parameters.get("query")
        locations = self.retrieve_locations(queries)
        title = self.generate_title(locations)
        parameters = self.parse_parameters(locations)
        self.db_curs.execute(ADD_HISTORY,
            (
                title,
                json.dumps(parameters),
                json.dumps(self.ux_info["project_list"]),
                json.dumps(self.parsed_evidence)
            )
        )
        self.db_conn.commit()
    
    def generate_title(self, locations: Optional[List[str]]) -> str:
        """Generates the title for saved project data.

        Args:
            locations (Optional[List[str]]): Retrieved locations from
                parameters.

        Returns:
            str: The generated title.
        """

        parameters = self.ux_info["parameters"]
        role = parameters["query"][0].split(" roles in ", 1)[0]
        str_date = datetime.now().strftime("%b %Y")

        if not locations:
            return f"{role} - United Kingdom - {str_date}"

        if len(locations) > 3:
            str_locations = ", ".join(locations[:1])
            locations_exp = f"{str_locations} (+{len(locations) - 2} more)"
            title = f"{role} - {locations_exp} - {str_date}"
        else:
            str_locations = ", ".join(locations)
            title = f"{role} - {str_locations} - {str_date}"
        
        return title
    
    def parse_parameters(self, 
        locations: Optional[List[str]]) -> Dict[str, Any]:
        """Parses parameters for the database.

        Args:
            locations (Optional[List[str]]): Retrieved locations from
                parameters.

        Returns:
            Dict[str, Any]: Parsed parameters.
        """

        parameters = self.ux_info["parameters"]
        queries = parameters.get("query")
        country = parameters.get("country")
        off_site = parameters.get("off_site")
        date_posted = parameters.get("date_posted")
        employment_types = parameters.get("employment_types")
        role = queries[0].split(" roles in ", 1)[0]

        if not locations:
            locations = "All UK Locations"
        
        if len(date_posted) == 0:
            date_posted = "All Time"

        if not employment_types:
            employment_types = "All Types"

        final_parameters = {
            "role": role,
            "locations": locations,
            "country": country,
            "off_site": off_site,
            "date_posted": date_posted,
            "employment_types": employment_types
        }

        return final_parameters
    
    def retrieve_locations(self, 
        queries: List[str]) -> Optional[List[str]]:
        """Retrieves locations from parameters.

        Args:
            queries (List[str]): Contains the list of queries.
        
        Returns:
            Optional[List[str]]: Contains the list of locations, or
                None if there are no inputted locations.
        """

        temp_locations = []
        for query in queries:
            if "United Kingdom" in query:
                break

            location = query.split(" in ", 1)[1].rstrip(".")
            temp_locations.append(location)
        
        if len(temp_locations) == 0:
            final_locations = None
        else:
            seen = set()
            final_locations = []
            for loc in temp_locations:
                if loc not in seen:
                    seen.add(loc)
                    final_locations.append(loc)
        
        return final_locations
    

        







