StackAmount = 64
DiamondHeight = 16
def CheckDiamondHeight():
    height = input("Input a height: ")
    height = int(height)
    if height > DiamondHeight:
        print("Too High")
    elif height == DiamondHeight:
        print("Right Level")
    else:
        print("Too Low")
def NumberToStackConversion():
    s = input("Input a number: ")
    s = int(s)
    s = s/StackAmount
    print(s)
def OreBlockConversion():
    s = input("Input an amount of items: ")
    s = int(s)
    s = s/9
    print(s)
def armourpieces():
    s = input("Input your amount of ores: ")
    s = int(s)
    if s < 4:
        print("Not enough for armour")
    elif s == 4:
        print("You can make boots")
    elif 5 <= s < 7:
        print("You can make a helmet")
    elif s == 7:
        print("You can make leggings")
    elif 8 <= s < 24:
        print("You can make a chestplate")
    else:
        print("You can make a full set of armour")
def menu():
    prompt = "1. Ask Diamond Height\n2. Number to Stack Conversion\n3. Ore Block Conversion\n4. Craftable armour"
    print(prompt)
    selection = input()
    if selection == "1":
        CheckDiamondHeight()
    elif selection == "2":
        NumberToStackConversion()
    elif selection == "3":
        OreBlockConversion()
    elif selection == "4":
        armourpieces()
menu()
#Homework: Create 2 new functions like the last two (Be creative)
#Create a global varible and use it at least twice| Like 16