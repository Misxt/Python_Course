# numbers = [1, 2, 3, 4, 5, 6]
# print(numbers)
# for i in range (len(numbers)):
#     print(numbers[i]+10)
#     if numbers[i]%2 == 1:
#         print(numbers[i])
names = ["Andrew", "Asa", "Kyle", 15, "Jayden", 13, "Sean"]
def stringPrint():
    for i in range (len(names)):
        if type(names[i]) == str:
            print(names[i])
def intPrint():
    for i in range (len(names)):
        if type(names[i]) == int:
            print(names[i])
# def starting_with_a():
#     result = [val for val in names if val.startswith("a")]
#     print(result)
stringPrint()
intPrint()
# starting_with_a()
#Homework: Finish the inPrint function
#Make a new function called starting with a
#Keep in mind the list is dynamic