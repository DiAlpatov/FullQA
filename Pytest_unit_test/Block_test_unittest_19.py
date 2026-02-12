import unittest
import requests

### Для того что бы запустить тесты, функции,классы название файла должно называться с test . Сам запуск  python -m unittest -v

class TestPostApi(unittest.TestCase):

  def setUp(self):
    body = {
     "title": "ewef13123gerg",
     "body": "qqqq",
     "userId": 1
    }
    headers = {'Content-Type': 'application/json'}
    responce = requests.post(
      f'https://jsonplaceholder.typicode.com/posts',
      json=body, 
      headers=headers
    )
    self.post_id = responce.json()['id']
    print(f'Answer post created:{self.post_id}')
  
  def tearDown(self):
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}')
    print(f'Post deleted {self.post_id}')
  

class TestIndepended(unittest.TestCase):
  def test_get_all_post(self):
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    self.assertNotEqual(len(response), self.post_id)  ### Внутренние методы юнит теста сравниваем длину с числом 100


  def test_add_post(self):
    body = {
      "title": "ewef13123gerg",
      "body": "qqqq",
      "userId": 1
    }
    headers = {'Content-Type': 'application/json'}
    responce = requests.post(
      f'https://jsonplaceholder.typicode.com/posts',
      json=body, 
      headers=headers
    )
    self.assertEqual(responce.status_code, 201)
    self.assertEqual(responce.json()['id'], 101)

  def test_get_one_post(self):
    responce = requests.get(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}').json()
    self.assertEqual(responce['id'], self.post_id)

