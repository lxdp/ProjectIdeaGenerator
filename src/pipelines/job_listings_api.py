import os
import http.client
from typing import Dict, Any
from urllib.parse import urlencode
from typing import List, Optional, Tuple

from dotenv import load_dotenv
load_dotenv()

from src.schemas.jsearch_user_view import (
    UserJobSearchResponse,
    UserJobSearchResponses,
    UserJobListing,
    JobHighlights,
    ApplyOption,
    Parameters
)

class JobListingsApi():
    """Class for parsing job listing data from OpenWebNinja API.
    
    This class handles API authentication, request building, and response 
    parsing for job search queries.
    """

    def __init__(
        self, 
        role: str,
        uk_locations: Optional[List[str]],
        date_posted: Optional[str],
        off_site: Optional[bool],
        employment_types: Optional[List[str]]
    ):
        """Initialize JobListingsApi instance.

        Args:
            role (str): Job role or keyword to search for.
            uk_locations (Optional[List[str]]): List of UK city names, or None 
                if no location filter is applied.
            date_posted (Optional[str]): Date filter for job postings, or None 
                if no date filter is applied.
            off_site (Optional[bool]): Boolean flag to filter for remote/hybrid 
                positions, or None if no off_site filter is applied.
            employment_types (Optional[List[str]]): List of employment types 
                to filter by, or None if no employment_types filter is applied.
        """

        self.role = role
        self.uk_locations = uk_locations
        self.date_posted = date_posted
        self.off_site = off_site
        self.employment_types = employment_types

        self.api_key = os.getenv("OPEN_WEB_NINJA_API_KEY")
        self.conn = http.client.HTTPSConnection("api.openwebninja.com")
    
    def run(self) -> UserJobSearchResponses:
        """Main orchestration workflow method. (Alter when return type is found).

        Returns:
            UserJobSearchResponses: List of the schema for the parsed job
                search response.
        """

        uk_locs = [None] if self.uk_locations == [] else self.uk_locations
        emp_types = [None] if self.employment_types == [] else self.employment_types

        job_listings = []
        query_list = []

        for uk_loc in uk_locs:
            for emp_type in emp_types:
                param_url, params = self.parse_params(uk_loc, emp_type)
                # retrieved_data = self.retrieve_own_data(param_url)
                # own_data = json.loads(retrieved_data)
                job_listing = self.parse_job_listing(self.EXAMPLE_RESPONSE)
                response = UserJobSearchResponse(root=job_listing)

                job_listings.append(response)
                query_list.append(params["query"])
    
        parsed_params = {
            "query": query_list,
            "country": "uk",
            "date_posted": self.date_posted,
            "off_site": self.off_site
        }

        if emp_types[0] is not None:
            parsed_params["employment_types"] = emp_types
        else:
            parsed_params["employment_types"] = None
        
        job_search_response = {
            "parameters": Parameters(**parsed_params),
            "job_listings": job_listings
        }
        
        return UserJobSearchResponses(**job_search_response)

    def retrieve_own_data(self, params: str) -> str:
        """Retrieves job listings.

        Args:
            params (str): Contains parsed parameters.

        Returns:
            str: Returns job listings in string representation.
        """

        headers = {
            "x-api-key": self.api_key
        }

        endpoint = f"/jsearch/search{params}"
        self.conn.request("GET", endpoint, headers=headers)
        res = self.conn.getresponse()
        data = res.read()

        return data.decode("utf-8")
    
    def parse_params(self, 
        loc: Optional[str], 
        emp_type: Optional[str]) -> Tuple[str, Dict[str, Any]]:
        """Parses retrieved query parameters from frontend.

        Params:
            loc (Optional[str]): Contains UK location, or None
                if no location filter is applied.
            emp_type (Optional[str]): Contains employment type, or
                None if not employment type filter is applied.

        Returns:
            Tuple[str, Dict[str, Any]]: Returns parsed query parameters.
        """

        query = f"{self.role} roles in the United Kingdom"
        params = {"query": query, "country": "uk"}

        if loc is not None:
            params["query"] = f"{self.role} roles in {loc}."

        if self.date_posted:
            params["date_posted"] = self.date_posted

        if self.off_site is not None:
            params["off_site"] = str(self.off_site).lower()

        if self.employment_types is not None:
            params["employment_types"] = emp_type

        

        return f"?{urlencode(params)}", params
    
    def parse_apply_options(self, 
        job: Dict[str, Dict]) -> List[ApplyOption]:
        """Populates a list of ApplyOption schemas.

        Args:
            job (Dict[str, Dict]): Retrieved data from OpenWebNinja API.
        
        Returns:
            List[ApplyOption]: List of the schema for parsed apply
                options data.
        """

        apply_options = []
        for app_opts in job["apply_options"]:
            app_opt_vals = {
                "publisher": app_opts.get("publisher"),
                "apply_link": app_opts.get("apply_link"),
                "is_direct": app_opts.get("is_direct")
            }

            apply_options.append(ApplyOption(**app_opt_vals))
        
        return apply_options
    
    def parse_job_highlights(self,
        job: Dict[str, Any]) -> JobHighlights:
        """Populates a JobHighlights schemas.

        Args:
            job (Dict[str, Any]): Retrieved data from OpenWebNinja API.
        
        Returns:
            JobHighlights: The schema for parsed job highlights
                data.
        """

        job_high = job["job_highlights"]
        job_high_vals = {
            "Qualifications": job_high.get("Qualifications"),
            "Responsibilites": job_high.get("Responsibilities"),
            "Benefits": job.get("job_benefits")
        }
        
        return JobHighlights(**job_high_vals)
    

    def parse_job_listing(self, 
        own_data: Dict[str, Dict]) -> List[UserJobListing]:
        """Populates a list of UserJobListing schemas.

        Args:
            own_data (Dict[str, Dict]): Retrieved data from OpenWebNinja API.
        
        Returns:
            List[UserJobListing]: List of the schema for parsed 
                job listing data.
        """

        job_listings = []
        for job in own_data["data"]:
            apply_options = self.parse_apply_options(job)
            job_highlight = self.parse_job_highlights(job)
            jl_values = {
                "job_id": job.get("job_id"),
                "job_title": job.get("job_title"),
                "employer_name": job.get("employer_name"),
                "employer_logo": job.get("employer_logo"),
                "employer_website": job.get("employer_website"),
                "job_location": job.get("job_location"),
                "job_city": job.get("job_city"),
                "job_state": job.get("job_state"),
                "job_country": job.get("job_country"),
                "job_is_remote": job.get("job_is_remote"),
                "job_employment_type": job.get("job_employment_type"),
                "job_employment_types": job.get("job_employment_types"),
                "job_posted_at": job.get("job_posted_at"),
                "job_posted_at_timestamp": job.get("job_posted_at_timestamp"),
                "job_posted_at_datetime_utc": job.get("job_posted_at_datetime_utc"),
                "job_salary": job.get("job_salary"),
                "job_min_salary": job.get("job_min_salary"),
                "job_max_salary": job.get("job_max_salary"),
                "job_salary_period": job.get("job_salary_period"),
                "job_apply_link": job.get("job_apply_link"),
                "job_apply_is_direct": job.get("job_apply_is_direct"),
                "apply_options": apply_options,
                "job_description": job.get("job_description"),
                "job_highlights": job_highlight,
                "job_benefits": job.get("job_benefits"),
                "job_publisher": job.get("job_publisher"),
            }

            job_listings.append(UserJobListing(**jl_values))

        return job_listings

        

