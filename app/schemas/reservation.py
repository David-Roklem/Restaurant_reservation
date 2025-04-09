from pydantic import BaseModel, Field
from datetime import datetime


class ReservationBase(BaseModel):
    customer_name: str = Field(max_length=50)
    table_id: int
    reservation_time: datetime
    duration_minutes: int


class ReservationRead(ReservationBase):
    id: int


class ReservationCreate(ReservationBase):
    pass
