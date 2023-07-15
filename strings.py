number = "6"
if not number.isnumeric():
    print("Invalid input")

sentence = "Hello, how are you"
if "you" in sentence:
    print("Preply")
sentence1, sentence2 = sentence.split(",")
print(sentence1)
print(sentence2)
print(sentence1.upper())
print(sentence1.lower())
sentence1.replace