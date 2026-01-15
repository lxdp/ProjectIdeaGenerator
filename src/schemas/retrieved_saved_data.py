from typing import List, Union, Optional

from pydantic import RootModel

from src.schemas.base import _BaseModel
from src.schemas.project_gen import ProjectList, ProjectIdeaEvidence

class DataBaseParameters(_BaseModel):
    role: str
    country: str
    off_site: bool
    locations: Union[str, List[str]]
    date_posted: Optional[str]
    employment_types: Union[str, List[str]]


class SavedData(_BaseModel):
    id: int
    title: str
    parameters: DataBaseParameters
    project_list: ProjectList
    evidence: ProjectIdeaEvidence

class SavedDataList(RootModel):
    root: List[SavedData]