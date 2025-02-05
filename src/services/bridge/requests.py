from pydantic import BaseModel

class RequestDataStructure(BaseModel):
    table: str
