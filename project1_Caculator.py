#Input two numbers and one symbol
number1 = input("Input your first number: ")
number2 = input("Input your second number: ")
operation = input("Input a symbol for your operation (+, -, *, /): ")
if not number1.isnumeric():
    print("Number 1 is invalid")
    exit()
if not number2.isnumeric():
    print("Number 2 is invalid")
    exit()
number1 = int(number1)
number2 = int(number2)
if operation == "+":
    answer = (number1+number2)
elif operation == "-":
    answer = (number1-number2)
elif operation == "*":
    answer = (number1*number2)
elif operation == "/":
    answer = (number1/number2)
else:
    print("The operation is not correct")
    exit()
print(f"Here is your answer: {answer}")

#Homework: 1. Choose three more string methods (Easier ones) and explain them (Just this one)
#2. (Difficult), you input two numbers and a symbol, put that all in one line (Example, 2+2)