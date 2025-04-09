from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from routers.exceptions import entity_not_found_ex, table_reserved_ex
from services import reservation as reservation_crud
from database import db_helper
from schemas.reservation import ReservationCreate, ReservationRead

router = APIRouter(prefix="/reservations", tags=["Reservations"])


@router.get("/", response_model=list[ReservationRead])
async def get_reservations(session: AsyncSession = Depends(db_helper.get_session_dependency)):
    reservations = await reservation_crud.get_all_reservations(session=session)
    return reservations


@router.post("/", response_model=ReservationCreate)
async def create_reservation(
    data_create: ReservationCreate,
    session: AsyncSession = Depends(db_helper.get_session_dependency),
):
    table_id = data_create.table_id
    res = await reservation_crud.create_reservation(
        session=session,
        reservation_create=data_create,
    )
    if res == "Reserved":
        raise table_reserved_ex(table_id, "Table")
    if res:
        return res
    raise entity_not_found_ex(table_id, "Table")


@router.delete("/{reservation_id}", response_model=ReservationRead)
async def delete_reservation(
    reservation_id: int,
    session: AsyncSession = Depends(db_helper.get_session_dependency),
):
    reservation = await reservation_crud.delete_reservation(
        session=session,
        reservation_id=reservation_id,
    )
    if reservation:
        return reservation

    raise entity_not_found_ex(reservation_id, "Reservation")
