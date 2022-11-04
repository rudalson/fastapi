from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def index():
    return {'data': {'name': 'kmpak'}}


@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs list'}
    else:
        return {'data': f'{limit}  blogs list'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    return {'data': {'1', '2'}}


@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}


@app.get('/about')
def about():
    return {'data': 'about page'}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f"Blog is created with title as {blog.title}"}
