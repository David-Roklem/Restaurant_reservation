from datetime import datetime, timedelta
from sqlalchemy import select, Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from models.reservation import Reservation


async def get_reservations_upon_table(session: AsyncSession, table_id: int) -> Sequence | None:
    """Возвращает все брони по данному столику."""
    result = await session.execute(select(Reservation).where(Reservation.table_id == table_id))
    if not result:
        return None
    reservations = result.scalars().all()
    return reservations


async def check_if_already_reserved(session: AsyncSession,
                                    table_id: int,
                                    reservation_time: datetime,
                                    duration_minutes: int) -> bool:
    """Проверяет занят ли конкретный столик в определенные дату и время. Возвращает True если занят,
    в противном случае - False."""
    reservations: list[Reservation] = await get_reservations_upon_table(session, table_id)
    reservations_slots = []
    for r in reservations:
        reservations_slots.append(dict(reserved_slot_start=r.reservation_time,
                                       reserved_slot_end=r.reservation_time + timedelta(minutes=r.duration_minutes)))
    reservation_start = reservation_time.replace(tzinfo=None)
    reservation_end = (reservation_start + timedelta(minutes=duration_minutes)).replace(tzinfo=None)
    for slot in reservations_slots:
        if not any([
            reservation_start > slot["reserved_slot_end"],
            reservation_end < slot["reserved_slot_start"],
        ]):
            return True
    return False
