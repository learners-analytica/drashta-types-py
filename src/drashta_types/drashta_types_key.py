from enum import Enum

class AggOperations(Enum):
    SUM = "sum"
    COUNT = "count"
    MAX = "max"
    MIN = "min"
    AVG = "avg"


class MLTaskTypes(Enum):
    CLASSIFICATION = "classification"
    REGRESSION = "regression"
    TS_FORECAST = "ts_forecast"
    RANK = "rank"
    SEQ_CLASSIFICATION = "seq-classification"
    SEQ_REGRESSION = "seq-regression"
    SUMMARIZATION = "summarization"
