from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

import aladdin
from aladdin.app.core.config import settings
from aladdin.app.routers import dummy
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title=settings.PROJECT_NAME.title(), version=aladdin.__version__)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(dummy.router)

templates = Jinja2Templates(directory='templates')


@app.get('/')
def root():
    return {'message': 'Welcome to Aladdin'}


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})
