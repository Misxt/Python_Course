Books = ["Blitzed Brits", "Frightful First World War", "Barmy British Empire"]
while True:
    option = input("1. Borrow a Book\n2. Give a Book\n3. Check if a book exists\n4. Quit\n")
    if option == "1":
        Borrow = input("What Book Do You Want To Borrow? ")
        Books.remove(Borrow)
    if option == "2":
        Give = input("What book do you want to return? ")
        Books.append(Give)
    if option == "3":
        Check = input("What book do you want to see? ")
        if Check in Books:
            print("The book exists")
        else:
            print("This book does not exist")
    if option == 4:
        break

    print(Books)

#Homework: Finish all of the options
#Make it bulletproof
#Optional: Make all of the options a function