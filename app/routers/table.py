from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from services import table as table_crud
from database import db_helper
from schemas.table import TableCreate, TableRead
from routers.exceptions import entity_not_found_ex

router = APIRouter(prefix="/tables", tags=["Tables"])


@router.get("/", response_model=list[TableRead])
async def get_tables(session: AsyncSession = Depends(db_helper.get_session_dependency)):
    tables = await table_crud.get_all_tables(session=session)
    return tables


@router.post("/", response_model=TableCreate)
async def create_table(
    data_create: TableCreate,
    session: AsyncSession = Depends(db_helper.get_session_dependency),
):
    return await table_crud.create_table(
        session=session,
        table_create=data_create,
    )


@router.delete("/{table_id}", response_model=TableRead)
async def delete_table(
    table_id: int,
    session: AsyncSession = Depends(db_helper.get_session_dependency),
):
    table = await table_crud.delete_table(
        session=session,
        table_id=table_id,
    )
    if table:
        return table

    raise entity_not_found_ex(table_id, "Table")
