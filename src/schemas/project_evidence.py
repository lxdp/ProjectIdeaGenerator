from typing import List

from pydantic import ConfigDict, RootModel

from src.schemas.base import _BaseModel

class Match(_BaseModel):
    model_config = ConfigDict(frozen=True)
    
    project_title: str
    project_achievement: str
    job_title: str
    company_name: str
    qualification: str

class ProjectListRelevance(RootModel):
    root: List[Match]