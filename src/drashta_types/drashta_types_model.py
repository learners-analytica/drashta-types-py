from .drashta_types_key import MLTaskTypes

TModelMetadata = {
    "id": str,
    "name": str,
    "estimator": str,
    "task": MLTaskTypes,
    "date": str,
}
