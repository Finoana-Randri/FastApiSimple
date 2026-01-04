from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./book.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
#to create session with the db
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
#helper for table definition
Base = declarative_base()