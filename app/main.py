from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from repository import BooksRepository

app = FastAPI()

templates = Jinja2Templates(directory="../templates")
repository = BooksRepository()

def find_book_by_id(id):
    books = repository.get_all()
    present_book = None
    
    for book in books:
        if book['id'] == id:
            present_book = book
            
    return present_book


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/books/{id}/edit")
def get_book_form_by_id(request: Request, id: int):
    book = find_book_by_id(id)
    
    if book is None:
        raise HTTPException(status_code=404, detail="Not Found")
    
    return_dict = {}
    return_dict['book'] = book
    
    return templates.TemplateResponse(
        "books/book_update_form.html",
        {"request": request, 'result': return_dict}
    )
    
@app.post("/books/{id}/edit")
def update_book_form_by_id(
    id: int, 
    title: str = Form(...),
    author: str = Form(...),
    year: str = Form(...),
    total_pages: str = Form(...),
    genre: str = Form(...)
):    
    book = find_book_by_id(id)
    
    if book is None:
        raise HTTPException(status_code=404, detail="Not Found")
    
    updated_book = {
        'title': title,
        'author': author,
        'year': year,
        'total_pages': total_pages,
        'genre': genre
    }
    
    book['title'] = updated_book['title']
    book['author'] = updated_book['author']
    book['year'] = updated_book['year']
    book['total_pages'] = updated_book['total_pages']
    book['genre'] = updated_book['genre']
    
    return RedirectResponse(url=f"/books/{id}", status_code=303)
    
@app.post("/books/{id}/delete")
def delete_book_by_id(
    id: int  
):
    book = find_book_by_id(id)
    
    if book is None:
        raise HTTPException(status_code=404, detail="Not Found")
    
    repository.delete(id)
    return RedirectResponse(url="/books", status_code=303)

@app.get("/books/new")
def add_book_form(request: Request):
    return templates.TemplateResponse("books/add_book.html", {"request": request})

@app.post("/books/new")
def add_book(
    title: str = Form(...),
    author: str = Form(...),
    year: str = Form(...),
    total_pages: str = Form(...),
    genre: str = Form(...)
):
    book = {
        'id': repository.get_len() + 1,
        'title': title,
        'author': author,
        'year': year,
        'total_pages': total_pages,
        'genre': genre
    }
    
    repository.save(book)
    
    return RedirectResponse(url="/books/", status_code=303)

@app.get("/books")
def get_books(request: Request, page: int = 0):
    if page:
        start_elements = (page - 1) * 10
        if start_elements + 1 < repository.get_len():
            raise HTTPException(status_code=404, detail="Don't have such many elements")
        books = repository[start_elements:min(start_elements + 10, repository.get_len())]
    else:
        books = repository.get_all()[:10]
    return templates.TemplateResponse(
        "books/index.html",
        {"request": request, "books": books},
    )

@app.get("/books/{id}")
def get_book_by_id(request: Request, id: int):
    book = find_book_by_id(id)
            
    if book is None:
        raise HTTPException(status_code=404, detail="Book was not found")
    
    prev_book = find_book_by_id(id - 1)
    next_book = find_book_by_id(id + 1)
    
    return_dict = {}
    
    if prev_book:
        prev_book = f"http://127.0.0.1:8000/books/{id - 1}"
        return_dict['prev_book'] = prev_book
    if next_book:
        next_book = f"http://127.0.0.1:8000/books/{id + 1}"
        return_dict['next_book'] = next_book
        
    return_dict['request'] = request
    return_dict['book'] = book
    
    return templates.TemplateResponse(
        "books/book_single.html",
        {"request": request, 'result': return_dict}
    )
    

    
# (сюда писать решение)

# (конец решения)
