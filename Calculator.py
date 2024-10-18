#Create a simple calculator in Python.

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
operator = input("Enter the Operator: ")
if operator == '+':
  print("Sum = ",num1 + num2)
elif operator == '-':
  print("Subtraction = ",num1 - num2)
elif operator == '*':
  print("Multiplication = ",num1 * num2)
elif operator == '/' and num2 != 0:
  print("Division = ",num1 / num2)
else:
  print("Error")
