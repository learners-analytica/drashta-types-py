from pydantic import BaseModel
from typing import Any, List

TDataArray = List[Any]

TColumnNames = List[str]
class TDataSeriesMinimal(BaseModel):
    column_name : str
    column_type : str
class TDataSeriesHead(TDataSeriesMinimal):
    column_is_key: bool

class TDataSeriesMetadata(BaseModel):
    column_avg: float
    column_min: float
    column_max: float
    column_count: int
    column_distinct : int

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