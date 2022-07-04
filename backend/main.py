from api.base import api_router
from db.base import Base
from db.session import engine
from core.config import settings

from fastapi import FastAPI


def include_router(app):
    app.include_router(api_router)

def create_tables():
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION
    )
    include_router(app)
    create_tables()
    return app

app = start_application()

@app.get("/")
def root():
    return {"msg": "I am Root!"}
