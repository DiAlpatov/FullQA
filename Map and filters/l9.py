summer = True
if summer is True: # можно сократить до if summer:
  print("efef")
else:
  print("second")

a = 'weweg'
if a:  # если строка не пустая то она TRUE
  print('reger')

a = 0
if a:  # если число не 0 то тру иначе фалсе
  print('reger')

arr = [1,2,3,4,5]
print(max(arr))
# или

arr = [1,2,3,4,5]
count = 0
for x in arr:
  if x > count:
    count = x
print(count)

print(sorted(arr))
print(sorted(arr, reverse=True))
arr.sort()
print(arr)
arr.sort(reverse=True)

ml = [1,2,3,4,5]

def multi(x):
  return x*3

new_ml = map(multi, ml)
print(list(new_ml))



ml = [1,2,3,4,5]

new_ml = map(lambda x: x * 2, ml) # лямда вызывает пустую функцию которая принимает значение и уможает на 2 каждый элем
print(list(new_ml))

ml = [1,2,3,4,5]

new_ml = map(lambda x: x * 2 if x > 10 else x*5, ml) # тернарник в лямде



array2 = [1,2,3,4,5,6,7,8,9]

newl2= []
for x in array2:
  if x % 2 == 0:
    newl2.append(x)
print(newl2)

def iseven(x):
  if x % 2 == 0:
    return True
  else:
    return False
newl3 = filter(iseven, array2)
print(list(newl3))

def iseven2(x):
    return x%2==0