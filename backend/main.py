from core.config import settings

from fastapi import FastAPI


def start_application():
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION
    )
    return app

app = start_application()

@app.get("/")
def root():
    return {"msg": "I am Root!"}
