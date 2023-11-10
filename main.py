#Tuyet Nguyen CS135-03 Calculator
import math

def addition(a,b):
  return a+b

def subtraction(a,b):
  return a-b

def multiplication(a,b):
   return a*b

def division(a,b):
   return a/b

while True:
  
   operator = input("Enter the operation: +,-,*,/,q' to exit,'sin', 'cos','sqrt', '^'as esponent")
   if operator == 'q':
         break
   elif operator == "sin":
     x = float(input("Enter a number:"))
     value = math.sin(x)
     print(f"{operator}({x}) = {value}")
   elif operator == 'cos':
     x = float(input("Enter a number:"))
     value = math.cos(x)
     print(f"{operator}({x}) = {value}")
   elif operator == 'sqrt':
     x = float(input("Enter a number:"))
     value = math.sqrt(x)
     print(f"{operator}({x}) = {value}")
   elif operator == '^':
     x = float(input("Enter a  number:"))
     y = float(input("Enter the exponent:"))
     value = math.pow(x,y)
     print(f"({x} power {y}) = {value}")
   elif operator == "+":
     x = float(input("Enter the first number:"))
     y = float(input("Enter the second number:"))
     value = addition(x,y)
     print(f"{x} {operator} {y} = {value}")
   elif operator == "-":
     x = float(input("Enter the first number:"))
     y = float(input("Enter the second number:"))
     value = subtraction(x,y)
     print(f"{x} {operator} {y} = {value}")
   elif operator  == '*':
     x = float(input("Enter the first number:"))
     y = float(input("Enter the second number:"))
     value = multiplicationn(x,y)
     print(f"{x} {operator} {y} = {value}")
   elif operator  == '/':
     x = float(input("Enter the first number:"))
     y = float(input("Enter the second number:"))
     if y == 0:
       print("Cannot perform division by 0!")
     else:
        value = division(x,y)
        print(f"{x} {operator} {y} = {value}")
   elif operator == "q":
     break
   else:
     print("Please enter the valid operation")
