from pydantic import BaseModel


class TableBase(BaseModel):
    name: str
    seats: int
    location: str


class TableRead(TableBase):
    id: int


class TableCreate(TableBase):
    pass
