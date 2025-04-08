from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text, String, SmallInteger
from .base import Base

if TYPE_CHECKING:
    from reservation import Reservation


class Table(Base):

    __tablename__ = "tables"

    name: Mapped[str] = mapped_column(String(50), nullable=False)
    seats: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    location: Mapped[str] = mapped_column(Text)

    reservations: Mapped[list["Reservation"]] = relationship(back_populates="tables")

    def __repr__(self):
        return f"Table(name={self.name}, seats={self.seats})"
