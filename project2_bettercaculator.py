sentence = input("Write an equation: ")

def conversion(s):#S is a local varible, only applies in this function
    if not s.isnumeric():
        print("A number is invalid")
        exit()
    return int(s)#This gives back an interger
def convert_sentence_to_number(c,operator):
    number1,number2 = c.split(operator)
    number1 = conversion(number1)
    number2 = conversion(number2)
    return (number1,number2)
if "+" in sentence:
    number1,number2 = convert_sentence_to_number(sentence,"+")
    answer = number1+number2
elif "-" in sentence:
    number1,number2 = convert_sentence_to_number(sentence,"-")
    answer = number1-number2
elif "**" in sentence:
    number1,number2 = convert_sentence_to_number(sentence,"**")
    answer = number1**number2
elif "*" in sentence:
    number1,number2 = convert_sentence_to_number(sentence,"*")
    answer = number1*number2
elif "/" in sentence:
    number1,number2 = convert_sentence_to_number(sentence,"/")
    answer = number1/number2
elif "^" in sentence:
    number1,number2 = convert_sentence_to_number(sentence,"^")
    answer = number1**number2
else:
    print("Invalid operation")
    exit()
answer = str(answer)
print("Here is your answer: " + answer)
#Homework: Finish this
#Do the power of two in another file and then do it in the caculator