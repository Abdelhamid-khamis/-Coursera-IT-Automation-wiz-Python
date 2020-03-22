
if 5 > 2:
    print("Five is greater than two!")
if 5 > 2:
  print("Five is greater than two!")

txt ="Hello world"
txt.replace("H","J")
txt.format()
''' 
fruits = ["apple","banana"]
fruits.insert(1,"orange")
fruits.remove("orange")
print(fruits)
 '''
# Hey 
''' fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
fruits.remove("banana")

print(fruits)
 '''

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.setdefault("color","red")
#car.update("check")
car["result"]="pass"
print(car)

print("Yes") if 5>2 else print("No")

y= lambda a: a+5
print (y(5))

Annon = lambda vr: (vr+2)**2
Annon(15)
print(type(Annon(10)))



def PercentageCalculator(Grade,FullGrade):
    result = Grade / FullGrade
    lambda FinalResult: result * 100
    return
    

PercentageCalculator(1000,1500)

#   Created Student(class) which inherited his features from Person which is to print his first name(Method)
class Person:   # class
    def __init__(self, fname):
        self.firstname = fname
    def printname(self):
        print(self.firstname) # Method
class Student(Person):
  pass
Khamis = Student("Abdelhamid") # Object
Khamis.printname()

#   Created Pitbull(class) which inherited his features from Dogs
class Dogs:
    def __init__ (self,breed,name,age,color):
        self.breed = breed #method
        self.name = name
        self.age = age
        self.color = color

class Pitbull(Dogs):
    pass
Amigo =Dogs("Rottweiler","Amigo",2.5,"Brown") #object
print(Amigo.breed)
print(Amigo.age)

#   Created an Anfield(class) which inherited his features from Stadium which is to print his first name(Method)
class Stadium(object):
    def __init__(self,name,capacity,TurfTexture,TurfLength):
        self.name=name # Method
        self.capacity=capacity
        self.TurfTexture=TurfTexture
        self.TurfLength=TurfLength
class Anfield(Stadium):
    pass
CampNou = Stadium("CampNou",80000, "bahia","long")
Anfield = Stadium("Anfield",53394, "GrassMaster ","Moderate")

print(CampNou.TurfTexture)

import math
print(dir(math))
import numpy
print(dir(numpy))
import hamidolib as hl
hl.greeting("Abdo")
print("Five is greater than two!") if 5 > 2 else print("No")
print (u"أحمد ماذا تفعل")

