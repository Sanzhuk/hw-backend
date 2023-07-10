from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from .repository import BooksRepository

app = FastAPI()

templates = Jinja2Templates(directory="templates")
repository = BooksRepository()


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/books")
def get_books(request: Request):
    books = repository.get_all()
    return templates.TemplateResponse(
        "books/index.html",
        {"request": request, "books": books},
    )


# (сюда писать решение)


# (конец решения)
