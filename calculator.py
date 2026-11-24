print("===MY CALCULATOR===")
print("1. Addition")
print("2. Subtraction")
print("3, Multiplication")
print("4. Division")
choice=int(input("Choose an operation:"))
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if choice == 1:
 print("Result:",num1+num2)
elif choice == 2:
 print("Result:",num1-num2)
elif choice == 3:
 print("Result:",num1*num2)
elif choice == 4:
 if num2!=0:
  print("Result:",num1/num2)
 else :
  print("Cannot divide by zero")
else:
 print("Invalid choice")
