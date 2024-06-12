operator=input("enter the operator : ")
print("Addition = '+")
print("Subtraction = '-")
print("Multiplication = '*")
print("Divison = '/")
print("operator : ",operator)
x=float(input("enter the first number : "))
y=float(input("enter the second number : "))
if operator == '+':
    result = x+y
    print("addition of two numbers:",result)
elif operator == '-':
    result = x-y
    print("subtraction of two numbers:",result) 
elif operator == '*':
    result = x*y
    print("multiplication of two numbers:",result)
elif operator == '/':
   if y != 0:
     result = x/y
     print("divison of two numbers:",result)
   else:
     print("Invalid input")  
else:
    print("Invalid input")               