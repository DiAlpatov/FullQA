def func1(give_me_func):
  print('before')
  give_me_func()
  print('after')

def simple1():
  print('simple1')

def simple2():
  print('simple2')

simple1()
simple2()

func1(simple1)
func1(simple2)

def simple3():
  print("I")
  print("love")
  print("PY")

func1(simple3)







def add_text(func):

    def wrapepr():
      print('before')
      func()
      print("after")

    return wrapepr

@add_text
def sim1():
  print('blablaq1')

@add_text
def sim2():
  print('ergrg22222')

sim1()
sim2()

#ewfwef