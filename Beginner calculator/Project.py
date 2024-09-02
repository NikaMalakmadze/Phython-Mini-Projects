#Simple Calculator Program

num1 = float(input(f"Please enter First Number: "))     #The first number variable
num2 = float(input(f"Please enter Second Number: "))    #The Second number variable

operation = input(f"Please enter the operation(+, -, /, *): ")   #The Math Operation variable

if operation == "+":

    print("your answer is:")
    print(num1 + num2)
elif operation == "-":

    print("your answer is:")
    print(num1 - num2)
elif operation == "/":

    print("your answer is:")
    print(round(num1 / num2, 3))    #When dividing, rounding the answer to thousands
elif operation == "*":

    print("your answer is:")
    print(num1 * num2)
else:
    print(f""" + operation + """ + " is not math operation!")      #If the input data is not a mathematical operation
