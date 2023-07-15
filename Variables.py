name = "Asa"#The varible name has the value "Asa"
print(name)
name_type = type(name)#The variable name_type stores the data type "string" or "int" of the varible name
#Type () figures out if "asa" is a string or int
print(name_type)

age = 13
print(age)
age_type = type(age)
print(age_type)

age = age+10#This is how you add 10 to a number
age = age+10
print(age)

name = name+" B"
print(name)

name = "Joe"
last_name = "Mcdonald"
age = 500
print(name+" "+last_name)
print(age)
age1 = 50
age2 = 90
average = (age+age1+age2)/3#This averages all three variables
print(average)
#+ is to do a sum, - is to subtract, / is to divide, and * is to multiply, exponents are **
print(age1**3)

sentence = "5"#Type = string
number = 8
sentence = int(sentence)#This converts the string of 5 to an interger with a value of 5
print(number+sentence)
sentence = str(sentence)
number = str(number)
print(number+sentence)#This is the concat of two strings

#user_input = input("Hello, please enter something: ")
#print("This was your input, "+user_input)

#ask the user for two numbers and print the +, -, *, and /
#Hint(Be careful, the user input will always be a string)
print("You will be asked for two numbers, please input them")#The one below does the same thing, but shows
number1 = input("Please enter your first number: ")#the answer and what it is in two different lines,
number2 = input("Please enter your second number: ")#this does it in one by converting them back to a
number1 = int(number1)#string
number2 = int(number2)
oneplustwo = (number1+number2)
oneplustwo = str(oneplustwo)
oneminustwo = (number1-number2)
oneminustwo = str(oneminustwo)
onetimestwo = (number1*number2)
onetimestwo = str(onetimestwo)
onedividedbytwo = (number1/number2)
onedividedbytwo = str(onedividedbytwo)
print("Here is your first number plus your second number: "+oneplustwo)
print("Here is your first number minus your second number: "+oneminustwo)
print("Here is your first number multiplied by your second number: "+onetimestwo)
print("Here is your first number divided by your second number: "+onedividedbytwo)
#print("Here is the sum of your two numbers")
#print(number1+number2)
#print("Here is your second number subtracted from the first")
#print(number1-number2)
#print("Here are your two numbers being multiplied")
#print(number1*number2)
#print("Here is your first number divided by your second")
#print(number1/number2)