from typing import List

from pydantic import RootModel

from src.schemas.base import _BaseModel

class Match(_BaseModel):
    project_title: str
    project_achievement: str
    job_title: str
    company_name: str
    qualification: str

class ProjectListRelevance(RootModel):
    root: List[Match]