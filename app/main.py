from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routers import get_and_post

app = FastAPI()
app.mount("/static", StaticFiles(directory="./app/static"), name="static")

# Include routers to app.
app.include_router(get_and_post.router)
