import requests

#def all_post():
#  response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
#  assert len(response) == 99 , 'Not all returned'

#all_post()

#def one_post():
#  post_id = 43
#  response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}').json()
#  assert response['id'] == post_id , 'Not all returned'

#one_post()


# СОздаем простой тест проверки статуса и того что в бд есть 101 пользователь

#def post():
#  body = {
#    "title": "ergerg",
#    "body": "qqqq",
#    "userId": "gregerg"
#  }
#  headers = {'Content-Type': 'application/json'}
#  responce = requests.post(
#    'https://jsonplaceholder.typicode.com/posts',
#    json=body, 
#    headers=headers
#  )
#  assert responce.status_code == 201 , "Not match"
#  assert responce.json()['id'] == 101, 'sucses'

#post()


### СОздадим и изменим один из постов
def new_post():
  body = {
    "title": "ergerg",
    "body": "qqqq",
    "userId": "gregerg"
  }
  headers = {'Content-Type': 'application/json'}
  responce = requests.post(
    'https://jsonplaceholder.typicode.com/posts',
    json=body, 
    headers=headers
  )
  return responce.json()['id']

def delete_post(post_id):
  responce = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')


def put_post():
  post_id = new_post()
  body = {
    "title": "ewef13123gerg",
    "body": "qqqq",
    "userId": "gregerg"
  }
  headers = {'Content-Type': 'application/json'}
  responce = requests.post(
    f'https://jsonplaceholder.typicode.com/posts/{post_id}',
    json=body, 
    headers=headers
  ).json()
  assert responce['title'] == 'ewef13123gerg'
  delete_post()

put_post()