from pydantic import BaseModel
from typing import Any, List

TDataArray = List[any]
class TDataSeriesHead(BaseModel):
    column_name: str
    column_type: str
    column_is_key: bool

class TDataSeriesMetadata(BaseModel):
    column_avg: float
    column_min: float
    column_max: float
    column_count: int

class TDataSeriesRaw(BaseModel):
    column_name: str
    column_type: str
    column_is_key: bool
    column_data: List[Any]

class TDataSeries(BaseModel):
    column_name: str
    column_type: str
    column_is_key: bool
    column_data: List[Any]
    column_avg: float
    column_min: float
    column_max: float
    column_count: int