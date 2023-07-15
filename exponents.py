sentence = input("Write an equation: ")
def convert_sentence_to_number(sentence,operator):
    number1,number2 = sentence.split(operator)
    number1 = conversion(number1)
    number2 = conversion(number2)
    return (number1,number2)
def conversion(s):#S is a local varible, only applies in this function
    if not s.isnumeric():
        print("A number is invalid")
        exit()
    return int(s)#This gives back an interger
def exponent(sentence):
    number1, number2 = sentence.split("^")
    number1 = conversion(number1)
    number2 = conversion(number2)
    return (number1,number2)
if "^" in sentence:
    sentence = exponent(sentence)
    answer = number1**number2
print(answer)
