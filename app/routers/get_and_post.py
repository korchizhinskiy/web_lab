from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates

from app.service.matrix import get_matrix

router = APIRouter()
templates = Jinja2Templates(directory="./app/templates")


@router.get("/home")
async def home_page(request: Request):
    matrix = get_matrix(5)
    return templates.TemplateResponse("index.html", {"request": request, "matrix": matrix})


@router.get("/matrix/matrix_get")
async def read_matrix_size_get(request: Request, matrix_size: str):
    matrix = get_matrix(int(matrix_size))
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "matrix": matrix},
    )


@router.post("/matrix/matrix_post")
async def read_matrix_size_post(request: Request, matrix_size: str = Form()):
    matrix = get_matrix(int(matrix_size))
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "matrix": matrix},
    )

    
