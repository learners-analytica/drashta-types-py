from pydantic import BaseModel

class RequestTrainAutoML(BaseModel):
    table: str
    columns: str
    target: str
    time_limit: str
    model_name: str
    train_split: str
    val_split: str
    test_split: str


class RequestPredictDataOnModel(BaseModel):
    model_id: str
    table: str
    columns: str

