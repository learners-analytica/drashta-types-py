from pydantic import BaseModel, Field

class DataSeries(BaseModel):
    seriesName: str = Field(..., description="Name of the series")
    seriesType: str = Field(..., description="Type of the series")
    seriesData: list = Field(..., description="Data of the series")


class TableColumnEntry(BaseModel):
    columnName: str = Field(..., description="Name of the column")
    columnType: str = Field(..., description="Type of the column")


class TableStructure(BaseModel):
    tableName: str = Field(..., description="Name of the table")
    tableColumns: list[TableColumnEntry] = Field(..., description="Columns of the table")

