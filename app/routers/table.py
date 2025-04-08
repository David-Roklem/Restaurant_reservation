from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from services.table import get_all_tables
from database import db_helper
from schemas.table import TableCreate, TableRead

router = APIRouter(prefix="/tables", tags=["Tables"])


@router.get("/", response_model=list[TableRead])
async def get_tables(session: AsyncSession = Depends(db_helper.get_session_dependency)):
    tables = await get_all_tables(session=session)
    return tables
