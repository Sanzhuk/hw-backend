from fastapi import FastAPI, Response, Query, HTTPException
from typing import List, Annotated

from .cars import create_cars

cars = create_cars(100)  # Здесь хранятся список машин
app = FastAPI()


@app.get("/")
def index():
    return Response("<a href='/cars'>Cars</a>")

# (сюда писать решение)

@app.get("/cars", response_model=List[dict])
def get_cars(
    page: int = Query(default=1, ge=1, le=100, description="The page number"),
    limit: int = Query(default=10, ge=1, le=100, description="The number of elements per page")
):
    start_idx = (page - 1) * limit
    end_idx = min(start_idx + limit, 100)
    
    return cars[start_idx:end_idx]

@app.get("/cars/{id}")
def get_cars_id(
    id: int,  
):
    for car in cars:
        if car["id"] == id:
            return car
        
    raise HTTPException(status_code=404, detail="Not found")

# (конец решения)
