from .drashta_types_key import MLTaskTypes
from .drashta_types_data import TDataSeriesMinimal

TModelMetadata = {
    "id": str,
    "name": str,
    "estimator": str,
    "task": MLTaskTypes,
    "date": str,
    "columns": list[TDataSeriesMinimal],
    "target":str
}
