from pydantic import BaseModel
from .drashta_types_key import MLTaskTypes


class TModelMetadata(BaseModel):
    id: str
    name: str
    estimator: str
    task: MLTaskTypes
    date: str
    data: list[str]
    target: str

