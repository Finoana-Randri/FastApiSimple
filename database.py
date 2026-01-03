from sqlalchemy import create_engine, false
from sqlalchemy.orm import declarative_base, sessionmaker, delarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./book.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":false}
)
#to create session with the db
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
#helper for table definition
Base = declarative_base()