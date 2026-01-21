from datetime import datetime

from fastapi import APIRouter,UploadFile,File, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from config.db_config import get_db
from crud import goods
from pathlib import Path

from fastapi.responses import FileResponse

import uuid



router = APIRouter(prefix="/api/goods", tags=["goods"])

@router.get("/goods_list")
async def get_user_list(skip: int = 0, limit: int = 100,db:AsyncSession=Depends(get_db)):
    user_list = await goods.get_goods(db, skip=skip, limit=limit)
    return {
        "code":200,
        "msg":"请求成功",
        "data":user_list
    }

# 1. 上传商品图片
@router.post("/upload_image")
async def upload_image(file: UploadFile = File(...)):
    # 安全检查：只允许图片
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="只允许上传图片")

    # 限制大小（5MB）
    if file.size > 5 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="文件不能超过5MB")

    # 生成唯一文件名
    suffix = Path(file.filename).suffix
    filename = f"{uuid.uuid4().hex}{suffix}"
    file_path = Path("uploads") / filename

    # 保存文件
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # 返回相对路径 URL（前端拼接 base URL）
    return {
        "code": 200,
        "msg": "上传成功",
        "data": {
            "url": f"/uploads/{filename}"
        }
    }

# 2. 提供静态文件访问（让 /uploads/xxx.jpg 可访问）
@router.get("/uploads/{filename}")
async def get_uploaded_image(filename: str):
    file_path = Path("uploads") / filename
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="图片不存在")
    return FileResponse(file_path)

@router.get("/images")
async def list_uploaded_images():
    upload_dir = Path("uploads")
    if not upload_dir.exists():
        return {
            "code": 200,
            "msg": "暂无图片",
            "data": []
        }

    image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"}
    images = []

    for file_path in upload_dir.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in image_extensions:
            stat = file_path.stat()
            images.append({
                "filename": file_path.name,
                "url": f"/uploads/{file_path.name}",
                "size": stat.st_size,  # 字节
                "upload_time": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                "extension": file_path.suffix.lower()
            })

    # 按上传时间倒序（最新在前）
    images.sort(key=lambda x: x["upload_time"], reverse=True)

    return {
        "code": 200,
        "msg": "获取成功",
        "data": images
    }

