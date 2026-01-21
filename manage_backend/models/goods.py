from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column

class Base(DeclarativeBase):
    update_time:Mapped[datetime] = mapped_column(DateTime,default=datetime.now,onupdate=datetime.now,comment='更新时间')
    create_time:Mapped[datetime] = mapped_column(DateTime, default=datetime.now, comment='创建时间')


class Goods(Base):
    __tablename__ = 'goods'
    id:Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True,comment="ID")
    name:Mapped[str] = mapped_column(String(50),comment="姓名",nullable=False)
    pic:Mapped[str] = mapped_column(String(100),comment="图片",nullable=False)
    org_price:Mapped[float] = mapped_column(Float,nullable=False,comment="原价")
    cur_price: Mapped[float] = mapped_column(Float, nullable=False, comment="现价")
    description:Mapped[str]=mapped_column(String(100),comment="描述")



