from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
import models,schemas
from database import engine,Base,SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 
@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/books/",response_model=schemas.Book)
def create_book(book:schemas.BookCreate,db:Session=Depends(get_db)):
    new_book = models.Book(**book.dit())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book