from pydantic import RootModel
from typing import List, Optional

from src.schemas.base import _BaseModel, Parameters

class JobHighlights(_BaseModel):
    Qualifications: Optional[List[str]]
    job_description: Optional[str]

class PromptData(RootModel):
    root: List[JobHighlights]

class JobInformation(_BaseModel):
    job_id: Optional[str] = None
    job_title: Optional[str] = None
    employer_name: Optional[str] = None
    job_location: Optional[str] = None
    job_is_remote: Optional[bool] = None
    job_employment_type: Optional[str] = None
    job_posted_at: Optional[str] = None
    job_apply_link: Optional[str] = None
    job_publisher: Optional[str] = None
    Qualifications: Optional[List[str]] = None

class ProjectIdeaEvidence(RootModel):
    root: List[JobInformation]

class GeneratedProject(_BaseModel):
    title: str
    problem_statement: str
    target_users: List[str]
    core_features: List[str]
    recommended_tech_stack: List[str]
    achieved_qualifications: List[str]

class ProjectList(_BaseModel):
    projects: List[GeneratedProject]

class UxInformation(_BaseModel):
    parameters: Parameters
    project_list: ProjectList
    evidence: ProjectIdeaEvidence

