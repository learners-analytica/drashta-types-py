from pydantic import BaseModel
from src.data.Tdata import DataSeries

class RequestDataStructurePOST(BaseModel):
    structure: list[TableStructure]

class RequestDataGET(BaseModel):
    data: list[DataSeries]
