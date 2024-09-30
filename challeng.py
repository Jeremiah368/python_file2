 # simple calculator

# the calculator must be a function

# this is a basic calculator

# ask for num1
# ask for num2

# print("choose an operator")
# print("")
# print("1, Addition")

# Operation = input("choose the operator u would like to perform")

# if oparation = "1" : add num 1 and num 2
# if opartion = "2" : minus num 2 from num 1
# If operation = "3" : divide num 1 by num 2, try and except
# if operation = "4" : multiply num 1 by num 2

# else: invalid

# again = input(" Do you want to perform another operation").lower()
# IF AGAIN == "Yes":
# Calculator()
# else: print("goodbye")

# Calculator()

print("This is a simple calcilator")

def calc():
    """This is a basic calculator"""
    print("this is a basic calculator app")
    print("Please enter your first num1")
    num1 = int(input())
    print("Please enter you num2")
    num2 = int(input())
    print("choose an operator")
    print("")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiply")
    print("4. divide")

    operation = input()

    if operation == "1":
        result = num1 + num2
        print(result)

    elif operation == "2":
        result = num2 - num1
        print(result)

    elif operation == "3":
        result = num1 * num2
        print(result)
        
    elif operation == "4":
        try:
            result = num1 / num2
            print(result)
        except ZeroDivisionError:
            print("Error, it can not be divide by zero")

    else:
        print("INVALID OPERATION")

    again = input("Do you wan to perform another operation: ").lower()


    
    if again == "yes":
        calc()
    else:
        print("goodbye")

calc()




