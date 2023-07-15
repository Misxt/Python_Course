# = is definition, == is a question
# == is equal to/> is greater than/< is less than/>= is greater than equal to/not means the oppisite
number = input("Please enter a number: ")
number = int(number)
if number > 5 and number < 10: #This is the condtion
    print("yes") #This is the consequence
elif number == 4 or number == 12:
    print("yes1")
else:
    print("no")
print("finish") #This will always be printed