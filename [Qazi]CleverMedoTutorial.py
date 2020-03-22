import turtle
#import tkinter
import time
# from vpython import *
# box(PrimitiveCalculator)
#window = tkinter.Tk(screenName="Snake")
#window.title("MySnake")

#MyTutle = turtle.Turtle()
""" def Square():
    #   Square
    MyTutle.forward(100)
    MyTutle.right(90)
    MyTutle.forward(100)
    MyTutle.right(90)
    MyTutle.forward(100)
    MyTutle.right(90)
    MyTutle.forward(100)

Square()
MyTutle.forward(100)
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
print("Thank you for using \"The Pirimitive Calculator\"")