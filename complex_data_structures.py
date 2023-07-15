# #String, like "Hello"
# #Interger, like 5
# #Float, like 0.8
# #Tuple, like (5,0.8,"hello"), you cannot modify this
# mytuple = (5,0.8,"hello")
# print(mytuple[0])
# print(type(mytuple[0]))
# print(mytuple[1])
# print(type(mytuple[1]))
# print(mytuple[2])
# print(type(mytuple[2]))
# number,number1,sentence = mytuple#This is called unpacking\
# print(number)
# print(number1)
# print(sentence)
# mytuple1 = (sentence, number1, number)#This is packing
# print(mytuple1)

#List/Arrays
colors = ["Red", "Blue", "Green", "Purple"]
print(colors)
print(colors[1:3])
print(colors[2])
#Add to a list
colors.append("Pink")
colors.insert(1,"Yellow")
print(colors)
#Modify a list
colors[3] = "Orange"
print(colors)
#Remove from a list
colors.remove("Pink")
colors.pop(4)
print(colors)
#Index to value and value to index
print(colors[2])
red_index = colors.index("Red")
print(red_index)
#Check if element is inside the list
if "Red" in colors:
    print("Red is in the list 'colors'")
print(colors)