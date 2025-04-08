from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.table import Table
from schemas.table import TableCreate


async def get_all_tables(session: AsyncSession) -> list:
    stmt = select(Table).order_by(Table.id)
    result = await session.scalars(stmt)
    return result.all()


async def get_table(session: AsyncSession, table_id: int) -> Table:
    result = await session.execute(select(Table).where(Table.id == table_id))
    table = result.scalar_one_or_none()
    if not table:
        return None


async def create_table(session: AsyncSession, table_create: TableCreate) -> Table:
    table = Table(**table_create.model_dump())
    session.add(table)
    await session.commit()
    return table


async def delete_table(session: AsyncSession, table_id: int) -> Table:
    table_to_delete = await get_table(session, table_id)
    if not table_to_delete:
        return None
    await session.delete(table_to_delete)
    await session.commit()
    return table_to_delete
