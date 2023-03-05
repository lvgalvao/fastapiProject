from fastapiproject.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_index():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'msg':'Hello world'}

def test_get_blog():
    id_blog = '14'
    response = client.get(f'/blog/{id_blog}')
    assert response.status_code == 200
    
    # Try to create a test to check if a not int type causes crash
    # assert response.json() == {'msg': f'Blog with {id_blog}'}
    