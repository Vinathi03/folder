from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
SQLALCHEMY_URL="postgresql+psycopg2://postgres:Feb$2024@localhost:5432/postgres"
engine=create_engine(SQLALCHEMY_URL)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close    