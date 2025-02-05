from pydantic import BaseModel

class ResponseTrainAutoML(BaseModel):
    model_id: str
    model_name: str
    model_file_path: str
    model_target: str
    model_task_type: str
    model_eval_metric: str

