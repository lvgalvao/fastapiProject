from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'msg':'Hello world'}

@app.get('/blog/{id}')
def get_blog(id: int):
    return {'msg': f'Blog with {id}'}
