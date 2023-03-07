from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional

app = FastAPI()

@app.get('/hello')
def index():
    return {'msg':'Hello world'}

@app.get('/blog/all')
def get_all_blogs(page = 1, page_size: Optional[int] = 10):
    return {'msg': f'All {page_size} blogs on page {page}'}


@app.get('/blog/{id}/comments/{comment_id}')
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {'msg': f'Blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
    return {'msg': f'Blog type {type}'}

@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'msg': 'Error'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'msg': f'Blog with {id}'}