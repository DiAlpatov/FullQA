import requests
import pytest

@pytest.fixture()
def new_post_id():
    body = {"title": "Имя книги","body": "структура книги","userId": 1}
    headers = {'Content-Type': 'application/json'}
    responce = requests.post(
      'https://jsonplaceholder.typicode.com/posts',
      json=body, 
      headers=headers
    )
    post_id = responce.json()['id']
    yield post_id
    print('Deleting the post')
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')

def test_get_one_post(new_post_id):
    responce = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}').json()
    assert responce['id'] == new_post_id

def test_get_all_post():
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100

def test_add_post():
    body = {"title": "ewef13123gerg","body": "qqqq","userId": 1}
    headers = {'Content-Type': 'application/json'}
    responce = requests.post(
      'https://jsonplaceholder.typicode.com/posts',
      json=body, 
      headers=headers
    )
    assert responce.status_code == 201
    assert responce.json()['id'] == 101

@pytest.fixture(scope='sesion')   ## сессия позволяет запускаться в любом месте,
def hello():  ##но проелдиться она только после последнего теста
    print('hello')
    yield
    print('bye')