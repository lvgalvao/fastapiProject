from fastapiproject.main import app
from fastapi.testclient import TestClient
from random import randrange

client = TestClient(app)

def test_index():
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.json() == {'msg':'Hello world'}

def test_get_blog_less_than_5():
    id_blog = randrange(1,4)
    response = client.get(f'/blog/{id_blog}')
    assert response.status_code == 200

def test_get_blog_greater_than_5():
    id_blog = randrange(6,10)
    response = client.get(f'/blog/{id_blog}')
    assert response.status_code == 404
    
    # Try to create a test to check if a not int type causes crash
    # assert response.json() == {'msg': f'Blog with {id_blog}'}
    