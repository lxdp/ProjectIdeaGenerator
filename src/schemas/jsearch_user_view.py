from __future__ import annotations

from typing import List, Optional

from pydantic import RootModel

from src.schemas.base import _BaseModel, Parameters

class ApplyOption(_BaseModel):
    # From job["apply_options"][]
    publisher: Optional[str] = None
    apply_link: Optional[str] = None
    is_direct: Optional[bool] = None

class JobHighlights(_BaseModel):
    # From job["job_highlights"]
    Qualifications: Optional[List[str]] = None
    Responsibilities: Optional[List[str]] = None
    Benefits: Optional[List[str]] = None


class UserJobListing(_BaseModel):
    # Identity + headline
    job_id: str
    job_title: str

    # Company
    employer_name: Optional[str] = None
    employer_logo: Optional[str] = None
    employer_website: Optional[str] = None

    # Where / remote
    job_location: Optional[str] = None
    job_city: Optional[str] = None
    job_state: Optional[str] = None
    job_country: Optional[str] = None
    job_is_remote: Optional[bool] = None

    # Employment
    job_employment_type: Optional[str] = None
    job_employment_types: Optional[List[str]] = None

    # Posted time (useful for UX sorting/labels)
    job_posted_at: Optional[str] = None
    job_posted_at_timestamp: Optional[int] = None
    job_posted_at_datetime_utc: Optional[str] = None

    # Compensation (often missing, but very user-relevant)
    job_salary: Optional[float] = None
    job_min_salary: Optional[float] = None
    job_max_salary: Optional[float] = None
    job_salary_period: Optional[str] = None

    # Applying
    job_apply_link: Optional[str] = None
    job_apply_is_direct: Optional[bool] = None
    apply_options: Optional[List[ApplyOption]] = None

    # Content / highlights
    job_description: Optional[str] = None
    job_highlights: Optional[JobHighlights] = None
    job_benefits: Optional[List[str]] = None

    # Provenance (can be shown as a small label in UX)
    job_publisher: Optional[str] = None

class UserJobSearchResponse(RootModel):
    # From EXAMPLE_RESPONSE (top-level)
    root: List[UserJobListing]

class UserJobSearchResponses(_BaseModel):
    parameters: Parameters
    job_listings: List[UserJobSearchResponse]