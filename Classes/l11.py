from abc import abstractmethod

class Group:
  pupils=True
  scholl_name = 42
  director = 'Boss'

  def __init__(self,name,piples_count,class_leader):
    self.name = name
    self.piples_count = piples_count
    self.class_leader = class_leader


  def study(self):
    print('something')

  @abstractmethod
  def move(self):
    pass            #"Это абстрактный метод.Указываем что действие мув должно в дочке быть реализовано другим разрабом

class PrimaryGroup(Group): # подкласс
  max_age = 11
  min_age = 6
  section = 'left'

  def __init__(self, name, piples_count, class_leader,house):
    super().__init__(name, piples_count, class_leader)
    self.house = house

  def move(self):
    print('run fast')

class Hight(Group):  # подкласс
  max_age = 18
  min_age = 14

  def move(self):
    print('GO slovly')

first_a = PrimaryGroup('one', '12','Misha','House mouse') # вызов подкласса с его данными
eleven_a = Hight('one sub', 20,'Dima')   # вызов подкласса с его данными


print(first_a.house)
print(first_a.min_age)
first_a.move()
eleven_a.move()

print(first_a.piples_count)
print(eleven_a.class_leader)