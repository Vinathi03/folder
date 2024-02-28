from sqlalchemy import Column,Integer,String ,LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from sqlalchemy import UniqueConstraint
Base=declarative_base()

class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True)
    username=Column(String,unique=True)
    email=Column(String,unique=True)
    password=Column(String)
    class Config:
        from_attributes=True
class Login(Base):
    __tablename__="login"
    username=Column(String,primary_key=True)
    password=Column(String)
# class FileMetadata(Base):
#     __tablename__='files' 
#     id=Column(Integer,primary_key=True)
#     filename=Column(String)
#     filesize=Column(Integer)
#     storage_location=Column(String)
class Table(Base):
    __tablename__="Data"
    sno=Column(Integer,primary_key=True)
    name=Column(String)
    text=Column(String)             