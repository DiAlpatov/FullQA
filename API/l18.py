import requests

#def all_post():
#  response = requests.get('https://jsonplaceholder.typicode.com/posts')
#  print(response.json()[1])

#all_post()

## version2 how too creater requests
# def all_post():
  # response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
  # print(response)

# all_post()

## version3 how too creater requests
# def one_post():
  # response = requests.get('https://jsonplaceholder.typicode.com/posts/1').json()
  # print(response)

# one_post()

## New POST 
#def post():
#  body = {
#    "title": "ergerg",
#    "body": "qqqq",
#    "userId": 1
#  }
#  headers = {'Content-Type': 'application/json'}
#  responce = requests.post('https://jsonplaceholder.typicode.com/posts',
#    json=body, 
#    headers=headers
#  ).json()
 # print(responce)

# post()

## Do new put 
#def put():
#  body = {
#    "title": "ergerg",
#    "body": "UUUUU",
#    "userId": 1
#  }
#  headers = {'Content-Type': 'application/json'}
#  responce = requests.put('https://jsonplaceholder.typicode.com/posts/42',
#    json=body, 
#    headers=headers
#  ).json()
#  print(responce)

#put()

## Do new patch 
#def patch():
#  body = {
#    "title": "ergerg",
#    "body": "UUUUU",
#    "userId": 1
#  }
#  headers = {'Content-Type': 'application/json'}
#  responce = requests.patch('https://jsonplaceholder.typicode.com/posts/42',
#    json=body, 
#    headers=headers
#  ).json()
#  print(responce)

#patch()

# Do delete person

#def delete():
#  responce = requests.delete('https://jsonplaceholder.typicode.com/posts/42')
#  print(responce.json())

#delete()



