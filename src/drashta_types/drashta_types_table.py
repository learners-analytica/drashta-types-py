from pydantic import BaseModel
from drashta_types_data import TDataSeries, TDataSeriesHead, TDataArray
from typing import List

class TTableHead(BaseModel):
    table_name: str
    

class TTableStructure(TTableHead):
    table_column_head_data: List[TDataSeriesHead]

class TTableMetaData(TTableHead):
    table_data_series: List[TDataSeries]

class TTableData(TTableHead):
    table_data_series: List[TDataArray]