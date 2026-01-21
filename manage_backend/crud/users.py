from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.users import User
from schemas.users import AddUserBase,UpdateUserBase


async def get_users(db:AsyncSession,skip:int=0,limit:int=10):
    stmt = select(User).offset(skip).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()

async def add_users(db:AsyncSession,user_params:AddUserBase):
    user_info = User(**user_params.__dict__)
    db.add(user_info)
    await db.commit()
    return {
        "code":200,
        "msg":"添加成功",
    }


async def delete_user(db:AsyncSession,userId:int):
    result = await db.execute(select(User).where(User.id==userId))
    user = result.scalars().one_or_none()
    if user is None:
        raise HTTPException(status_code=404)
    await db.delete(user)
    await db.commit()
    return {
        "code":200,
        "msg":user
    }

async def update_user(db:AsyncSession,user_params:UpdateUserBase,telephone_id:str):
    result = await db.execute(select(User).where(User.telephone == telephone_id))
    user_info = result.scalars().one_or_none()
    if user_info is None:
        raise HTTPException(status_code=404)
    user_info.name = user_params.name
    user_info.telephone = user_params.telephone
    user_info.address = user_params.address
    user_info.description = user_params.description
    user_info.role = user_params.role

    await db.commit()
    return {
        "code":200,
        "msg":"更新成功"
    }