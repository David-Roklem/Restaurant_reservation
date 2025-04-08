from models.table import Table
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


async def get_all_tables(session: AsyncSession) -> list:
    stmt = select(Table).order_by(Table.id)
    result = await session.scalars(stmt)
    return result.all()
