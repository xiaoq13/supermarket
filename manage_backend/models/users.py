from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column

class Base(DeclarativeBase):
    update_time:Mapped[datetime] = mapped_column(DateTime,default=datetime.now,onupdate=datetime.now,comment='更新时间')
    create_time:Mapped[datetime] = mapped_column(DateTime, default=datetime.now, comment='创建时间')

class User(Base):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True,comment="ID")
    name:Mapped[str] = mapped_column(String(50),comment="姓名",nullable=False)
    telephone:Mapped[str]=mapped_column(String(50),comment="手机号",unique=True,nullable=False)
    role:Mapped[str]=mapped_column(String(50),nullable=False,comment='角色')
    address:Mapped[str]=mapped_column(String(150),nullable=False,comment='地址')
    description:Mapped[str]=mapped_column(String(100),comment="描述")




