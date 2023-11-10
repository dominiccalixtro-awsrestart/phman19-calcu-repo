#variable used for the continuation of the program.
bool_val = True


#function for the continuation.
#will be called multiple times.
def continuation():
  global bool_val
  con = input("Would you like to try again? (Y for yes and N for no): ")
  if (con == "Y"):
    bool_val = True
  else:
    bool_val = False
    print("Thank you for using the calculator.")


#function for addition.
def addition(num1, num2):
  print("The sum of the 2 numbers is: ", num1 + num2)
  continuation()


#function for subtraction.
def subtraction(num1, num2):
  print("The difference of the 2 numbers is: ", num1 - num2)
  continuation()


#function for multiplication.
def multiplication(num1, num2):
  print("The product of the 2 numbers is: ", num1 * num2)
  continuation()


#function for division.
def division(num1, num2):
  if num2 != 0:
    print("The quotient of the 2 numbers is: ", num1 / num2)
  else:
    print("Cannot divide by zero")
  continuation()


#while loop for initialization of the program.
#will be reuse for the continuation.
while bool_val:
  oper = input("What operation do you want to perform? (+, -, *, /) ")
  num1 = input("Enter first number: ")
  num2 = input("Enter second number: ")

  #to confirm that the user entered an actual digit or number.
  #if not, they will be ask if they want to try again.
  if num1.isdigit() and num2.isdigit():
    num1 = float(num1)
    num2 = float(num2)
    if (oper == "+"):
      addition(num1, num2)
    elif (oper == "-"):
      subtraction(num1, num2)
    elif (oper == "*"):
      multiplication(num1, num2)
    elif (oper == "/"):
      division(num1, num2)
    else:
      print("Invalid Operator.")
      continuation()
  else:
    print("Please enter numerical values for the two numbers.")
    continuation()
