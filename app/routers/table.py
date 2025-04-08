<<<<<<< HEAD
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from services import table as table_crud
=======
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from services.table import get_all_tables
>>>>>>> 5d1428e902c0355410f174c9ba053a3d4e1541d8
from database import db_helper
from schemas.table import TableCreate, TableRead

router = APIRouter(prefix="/tables", tags=["Tables"])


@router.get("/", response_model=list[TableRead])
async def get_tables(session: AsyncSession = Depends(db_helper.get_session_dependency)):
<<<<<<< HEAD
    tables = await table_crud.get_all_tables(session=session)
    return tables


@router.post("/create", response_model=TableCreate)
async def create_table(
    data_create: TableCreate,
    session: AsyncSession = Depends(db_helper.get_session_dependency),
):
    return await table_crud.create_table(
        session=session,
        table_create=data_create,
    )


@router.delete("/delete/{table_id}", response_model=TableRead)
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

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Table #{table_id} not found!",
    )
=======
    tables = await get_all_tables(session=session)
    return tables
>>>>>>> 5d1428e902c0355410f174c9ba053a3d4e1541d8
