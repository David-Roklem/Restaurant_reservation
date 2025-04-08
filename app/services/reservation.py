from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from services.table import get_table
from models.reservation import Reservation
from schemas.reservation import ReservationCreate


async def get_all_reservations(session: AsyncSession) -> list:
    stmt = select(Reservation).order_by(Reservation.id)
    result = await session.scalars(stmt)
    return result.all()


async def get_reservation_upon_table(session: AsyncSession, table_id: int) -> list | None:
    result = await session.execute(select(Reservation).where(Reservation.table_id == table_id))
    if not result:
        return None
    reservations = result.scalars().all()


async def create_reservation(session: AsyncSession, reservation_create: ReservationCreate) -> Reservation:
    table_id = reservation_create.table_id
    table = await get_table(session, table_id)
    if not table:
        return None
    reservation = Reservation(**reservation_create.model_dump())
    session.add(reservation)
    await session.commit()
    return reservation


async def delete_reservation(session: AsyncSession, reservation_id: int) -> Reservation:
    result = await session.execute(select(Reservation).where(Reservation.id == reservation_id))
    reservation_to_delete = result.scalar_one_or_none()
    if not reservation_to_delete:
        return None
    await session.delete(reservation_to_delete)
    await session.commit()
    return reservation_to_delete
