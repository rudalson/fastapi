from fastapi import FastAPI
import schemas
import models
from database import engine

models.Base.metadata.create_all(engine)

app = FastAPI()


@app.post('/blog')
def create(request: schemas.Blog):
    return request
