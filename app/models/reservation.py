from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Integer, DateTime
from .base import Base

if TYPE_CHECKING:
    from table import Table


class Reservation(Base):

    __tablename__ = "reservations"

    customer_name: Mapped[str] = mapped_column(String(50), nullable=False)
    table_id: Mapped[int] = mapped_column(ForeignKey("tables.id"), nullable=False)
    reservation_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    duration_minutes: Mapped[int] = mapped_column(Integer, nullable=False)

    tables: Mapped["Table"] = relationship(back_populates="reservations")

    def __repr__(self):
        return (f"Reservation(customer_name={self.customer_name}, reservation_time={self.reservation_time}, "
                f"duration_minutes={self.duration_minutes})")
