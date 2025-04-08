from pydantic import BaseModel, ConfigDict


class TableBase(BaseModel):
    name: str
    seats: int
    location: str


class TableRead(TableBase):
    id: int


class TableCreate(TableBase):
    pass



# data = {
#     "name": "Table 1",
#     "seats": 10,
#     "location": "Amidst the space",
# }
# print(TableCreate(**data))
