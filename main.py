#Created just for testing-

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/blog')
def index(limit=10, published:bool = True, sort: Optional[str] = None):

    if published:
        return {'data': f'{limit} blogs from the db list'}
    else:
        return {'data': f'{limit} blogs db'}

@app.get('/about')
def about():
    return {'data':'about page'}

@app.get('/blog/{id}')
def show(id: int):
    return {'data' : id}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
    return blog


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)