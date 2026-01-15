from typing import Optional, List

from pydantic import ConfigDict, BaseModel

class _BaseModel(BaseModel):
    model_config = ConfigDict(extra="ignore")

class Parameters(_BaseModel):
    query: List[str]
    country: str
    date_posted: Optional[str] = None
    off_site: Optional[bool] = None
    employment_types: Optional[List[str]] = None