from vpython import *
''' import turtle
#import tkinter
import time
from vpython import *
# box(PrimitiveCalculator)
#window = tkinter.Tk(screenName="Snake")
#window.title("MySnake")

#MyTurtle = turtle.Turtle()
""" def Square():
    #   Square
    MyTurtle.forward(100)
    MyTurtle.right(90)
    MyTurtle.forward(100)
    MyTurtle.right(90)
    MyTurtle.forward(100)
    MyTurtle.right(90)
    MyTurtle.forward(100)

Square()
MyTurtle.forward(100)
Square()
time.sleep(10)
 """


def PrimitiveCalculator():
    num1 = float(input("Enter your 1st number: "))
    num2 = float(input("Enter your 2nd number: "))
    operation = str(input("Choose one operation or one operator to perform its calculations from the next four operations\n Add / Multiply / Divide / Substract: "))
    #   Sum

    if operation == "Add":
        print("The Result is ", num1 + num2)
        return
    if operation == "Multiply":
        print("The Result is ", num1 * num2)
    elif operation == "Divide" :
        try:
            print("The Result is ",num1 / num2)
        except ZeroDivisionError:
            print("Your 2nd number was Zero, Please Check it")
    elif operation == "Substract":
        print("The Result is ",num1 - num2)
    else:
        print("please revise your choice of operation \nwrite it as the same as it shown")


Quit="y"
while Quit != "n":
    PrimitiveCalculator()
    time.sleep(5)
    print("Type y to continue \nor type n to quit")
    Quit = str(input("Choose y/n: "))
print("Thank you for using \"The Primitive Calculator\"") '''

#   Solution 2
import math
import os
import random
import re
import sys


# My problem is: that when i input 18, it should give me "Weird" but it doesn't!
''' if __name__ == '__main__':
    n = int(input().strip())
    if n%2 != 0:
        print("Weird")
    elif n%2 == 0 and n in range (2,6):
        print("Not Weird")
    elif n%2 == 0 and n in range (6,21):
        print("Weird")
    elif n%2 == 0 and n > 20:
        print("Not Weird")
    else:
        print("None of the above options!") '''

#   Solution 3
''' if__name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b) '''

#Solution 4
""" if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i**2)
 """

''' 
from selenium import webdriver
get("https://www.youtube.com") 
'''

''' def CountDown(number):
    CountDownStartNumber = number
    while CountDownStartNumber >= 0:
        print(CountDownStartNumber)
        CountDownStartNumber -=1
    print ("Count down finished!")
CountDown(10) '''

''' def CelsiusConverter(Fahrenheit):
    return (Fahrenheit-32)*(9/5)
for Fahrenheit in range (0,101,10):
    print(Fahrenheit, CelsiusConverter(Fahrenheit))
 '''
