from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from config.db_config import get_db
from crud import users

from schemas.users import AddUserBase,UpdateUserBase



router = APIRouter(prefix="/api/users", tags=["users"])

@router.get("/user_list")
async def get_user_list(skip: int = 0, limit: int = 100,db:AsyncSession=Depends(get_db)):
    user_list = await users.get_users(db, skip=skip, limit=limit)
    return {
        "code":200,
        "msg":"请求成功",
        "data":user_list
    }

@router.post("/user_create")
async def add_user(user:AddUserBase,db:AsyncSession=Depends(get_db)):
    add_list = await users.add_users(db,user)
    return add_list

@router.delete("/user_delete")
async def delete_user(user_id:int,db:AsyncSession=Depends(get_db)):
    delete_user = await users.delete_user(db,user_id)
    return delete_user

@router.put("/user_update")
async def update_user(telephone_id:int,user:UpdateUserBase,db:AsyncSession=Depends(get_db)):
    update_user = await users.update_user(db,user,telephone_id)
    return update_user