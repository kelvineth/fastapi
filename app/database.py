from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

SQLACLCHEMY_DATABASE_URL= f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine=create_engine(SQLACLCHEMY_DATABASE_URL)

SessionLocal=sessionmaker(bind=engine ,autocommit=False,autoflush=False)

Base=declarative_base()


def get_db():
    db=SessionLocal()
    try:
        yield db
    
    finally:
        db.close()