from pydantic import BaseModel, Field


class TableBase(BaseModel):
    name: str = Field(max_length=50)
    seats: int = Field(gt=0, le=14)
    location: str = Field(max_length=100)


class TableRead(TableBase):
    id: int


class TableCreate(TableBase):
    pass
