from pydantic import BaseModel
class UserBase(BaseModel):
    username:str
    email:str
    password:str
class User(UserBase):
    id:int
    class Config:
        orm_mode=True
class LoginBase(BaseModel):
    username:str
    password:str
class Login(LoginBase):
    id:int
    class Config:
        orm_mode=True
# class FileMetadataBase(BaseModel):
#     filename:str
#     fiesize:int
#     storage_locati
class TableBase(BaseModel):
    sno:str
    name:str
    text:str        
class Table(TableBase):
    id:int
    class Config:
        orm_mode=True 
class DataBase(BaseModel):
    data:str
    class Config:
        orm_mode=True               
    