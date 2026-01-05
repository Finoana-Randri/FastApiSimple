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
    return {"message": "Hello-World"}

#create a new books
@app.post("/books/",response_model=schemas.Book)
def create_book(book:schemas.BookCreate,db:Session=Depends(get_db)):
    new_book = models.Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book
#all books
@app.get("/books/",response_model=list[schemas.Book])
def get_all_books(skip:int=0, limit:int = 100, db:Session=Depends(get_db)):
    books= db.query(models.Book).offset(skip).limit(limit).all()
    return books

# get book ny id
@app.get("/books/{book_id}",response_model=schemas.Book)
def get_book(book_id:int, db:Session=Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404,detail="Book Not Found")
    return book

#update book
@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id:int, updated:schemas.BookCreate, db:Session=Depends(get_db)):
    book= db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404,detail="Book Not Found")
    book.title = updated.title
    book.author = updated.title
    book.description = updated.title
    db.commit()
    db.refresh(book)
    return book

#delete book
@app.delete("/books/{book_id}", response_model=schemas.Book)
def delete_book(book_id:int , db:Session=Depends(get_db)): 
    book  = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book :
        raise HTTPException(status_code=404, detail="Book Not Found")
    db.delete(book)
    db.commit()
    return book


