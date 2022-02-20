from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import sys
from pathlib import Path
_app_root = str(Path(__file__).parent.parent.parent.absolute())
if _app_root not in sys.path:
    sys.path.append(_app_root)



import aladdin
from aladdin.app.core.config import settings
from aladdin.app.routers import dummy

app = FastAPI(title=settings.PROJECT_NAME.title(), version=aladdin.__version__)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dummy.router)

@app.get('/')
def root():
    return {'message': 'Welcome to Aladdin'}
