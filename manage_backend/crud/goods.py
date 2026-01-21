from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.goods import Goods
from schemas.users import AddUserBase,UpdateUserBase

async def get_goods(db:AsyncSession,skip:int=0,limit:int=10):
    stmt = select(Goods).offset(skip).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()

