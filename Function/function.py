#i = 0 
#while i < 5:
#  print('hello')
#  i += 1
#print("end")

#while True:
#  print('super loop') # бесконечный цикл

#while True:
#  inp = input('Enter somethong')
#  if inp == 'exit':
#    break
#  elif inp =='continue':
#    continue
#  elif len(inp) > 10:
#    print('Input is too long')
#  else:
#    print('inp is ok')
#print("BB")

#def calc(numb):
#  a=0
#  return numb
#print(calc(12))

#def power(n1, deg=2):
#  return n1**deg
#print(power(2,3))

#def sum_all(*args):
#  result = 0
#  for x in args:
#    result += x
#    return result
#print(sum_all(1,4,5,6,8))  

def price(t1,t2):
  print(f'Product {t1} price is {t2}')

price('wefwef',123)
price('wefwef',122523)


def products(**kwargs):
  print(kwargs)
  for x in kwargs.items():
    print(x)
products(l=2,f=3,erg=3030)

def products(**kwargs):
  print(kwargs)
  for x in kwargs.items():
    title,price=x
    print(f'Product {title} price is {price}')
products(l=2,f=3,erg=3030)