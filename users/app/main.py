from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from users import create_users

users = create_users(100)  # Здесь хранятся список пользователей
app = FastAPI()

templates = Jinja2Templates(directory="../templates")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# (сюда писать решение)

@app.get("/users", response_class=HTMLResponse)
def get_all_users(request: Request):
    return templates.TemplateResponse("users/index.html", {'request':request, 'result':users, 'result_len':len(users)})

@app.get("/users/{id}", name="user_detail")
def user_detail(request: Request, id: int):
    for user in users:
        if user['id'] == id:
            target_user = user
    
    return templates.TemplateResponse("users/user.html", {'request':request, 'result':target_user})

# (конец решения)
