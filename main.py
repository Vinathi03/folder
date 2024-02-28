from fastapi import FastAPI,UploadFile,File,HTTPException,Request
from fastapi.exception_handlers import RequestValidationError
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse,RedirectResponse,PlainTextResponse,HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Table,Intern,User,FileMetadata,Login
from typing import List,Optional
from jose import jwt,JWTError
from os,string,re,pdfplumber,shutil,uvicorn
app=FastAPI()
temapalates=Jinja2Templates(directory="tempalates")
SQLALCHEMY_DATABASE_URL="postgresql+psycopg2://postgres:FEB$2024@localhost:5432/postgres"
engine=create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
@app.get("/register",request_class=HTMLResponse)
async def register_po(request:Request):
    return temapalates.TemplateResponse("request.html",{"request":request})
static_directory=os.path.join(os.path.dirname(os.path.abspath()))
app.mount("/static",StaticFiles(directory="./tempalates/"),name="static")
@app.post("/register",response_class=HTMLResponse)
async def register(username:str,email:str,password:str,request:Request):
    session=SessionLocal()
    try:
        existing_user=session.query(User).filter(User.email==email).first()
        if existing_user:
            raise HTTPException(status_code=400,detail="Email address not registered")
        new_user=User(username=username,email=email,password=password)
        session.add(new_user)
        session.commit()
        return temapalates.TemapalateResponse("register.html",{"Request":request,"username":username,"email":email,"password":password})
    except Exception as e:
        print(f"An error occurred:{e}")
        raise HTTPException(status_code=500,detail="Internal server error")
    finally:
        session.close()
static_directory=os.path.join(os.path.dirname(os.path.abspath()),temapalates)
app.mount("/static",StaticFiles(directory="./tempalates/"),name="static")
@app.get("/login",response_class=HTMLResponse)  
async def login_po(request:Request):
    return temapalates.TemplateResponse("login.html",{"request":request})
@app.post("/login",response_class=HTMLResponse)
async def login(request:Request):
    session=None
    try:
        form=await request.form()
        username=request[username]
        password=request[password]
        session=SessionLocal()
        user=session.query(User).filter(User.username==username).first()
        if user is None or user.password!=password:
            raise HTTPException(status_code=401,detail="Invalid username or password")
        login_session=Login(username=username,password=password)
        session.add(login_session)
        session.commit()
        return temapalates.TemplateResponse("login.html",{"request":request,"username":username,"password":password})
    except Exception as e:
        print(f"An error occured during login:{str(e)}")
        raise HTTPException(status_code=500,detail=f"An error occurred  during login:{str(e)}")
    finally:
        if session:
            session.close()
static_directory=os.path.join(os.path.dirname(os.path.abspath()),temapalates)
app.mount("/static",StaticFiles(directory="./tempalates/"),name="static")
@app.post("/pdf_search",response_class=HTMLResponse)
async def pdf_search(file:UploadFile=File(...),keyword:str=None):
    session=SessionLocal()
    try:
        with open("uploaded_pdf.pdf","wb")as buffer:
            buffer.write(await file.read())
        extracted_words=set()
        with pdfplumber.open("uploaded_pdf.pdf") as pdf:
            for page in pdf.pages:
                page_text=page.extract_text()
                try:
                    page_text_split=page_text.split()
                except Exception as e:
                    print("Error splitting page text:",e)
                    continue
                for each_keyword in page_text_split:
                    if each_keyword==keyword:
                        table_entry=Table(name=keyword,text=keyword)    
                        session.add(table_entry)
                        session.commit()
                extracted_words.update(page_text_split)  
        result=[word for word in extracted_wordsif re.search(fr"\b{re.escape(keyword)}\b",word)]
        results="\n".join(result)
        return temapalates.TempalateResponse("upload.html",{"request":{},"keyword":keyword,"message":"is found" if keyword else "not found"})
    except Exception as e:
        print(f"An error occurred during PDF search:{str(e)}")
        raise HTTPException(status_code=500,detail=f"An error occurred during PDF search:{str(e)}")
    finally:
        session.close()
if __name__=="__main__":
    uvicorn.run(app,host='0.0.0.0'port=9000)                      



