# Инкапсуляция - Все данные объекта должны хранится в объекте.
# Ни кто не может менять данные объекта без его ведома

# НАследование объекты и их типы организуют иерархию типов. Дочерние типы наследуют
# свою функциональность от родительского класа расширяя и дополняя ее

# Полиморфизм - Способность классов менять свое поведение в зависимости от типов операции
# и операндов. Полиморфизм в программировании реализуется через перегрузку метода,
# либо через его переопределение



# data1.txt
{'Country':'Russia','avg_temp':-10}
# data1.txt
{'Country':'Turkey','avg_temp':30}

import json

class CountryData:

  def __init__(self,filename):
    self.filename = filename
    self.data = self.read_file()
    self.country = self.data["Country"]
    self.avg = self.data["avg_temp"]

  def read_file(self):
    file_data = open(self.filename, 'r')
    #data = file_data.read()
    data = json.load(file_data)
    file_data.close()
    return data

##data1 = read_file('FullQA/OOP/data1.txt')
##data2 = read_file('FullQA/OOP/data2.txt')
#print(data1['Country'])
#print(data2['Country'])

data1 = CountryData('FullQA/OOP/data1.txt')
print(data1.country)

data2 = CountryData('FullQA/OOP/data2.txt')
print(data2.avg)