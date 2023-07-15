import menu
database = {"Misxt":{"Level":10, "Playtime":8, "Friends":[], "Password":"Anki" }, "Joe":{"Level":9, "Playtime": 2, "Friends":["Misxt"], "Password":"Test"}}
def register():
    username = input("Input a username: ")
    password = input("Make a password: ")
    database[username] = {"Level":1, "Playtime":0, "Friends":[], "Password":password}
def login():
    username = input("Input your username: ")
    if username in database:
        password = input("Input your password: ")
        if password == database[username]["Password"]: 
            return(True)
        else:
            return(False)
    else:
        return(False)
def leaderboard():
    username = input("Whose leaderboard do you want to see? ")
    users_level = []
    users_level.append([username, database[username]["Level"]])
    for friends in database[username]["Friends"]:
        users_level.append([friends,database[friends]["Level"]])
    print(users_level)

def add_friend():
    username = input("Input your username: ")
    if username in database:
        newfriend = input("Who do you want to add as a friend? ")
        if newfriend in database:
            database[username]["Friends"].append(newfriend) 
            print("True")
        else:
            print("Only friends in the database, no imagiary friends")
    else:
        print("Username Invalid")
def remove_friend():
    username = input("Input your username: ")
    if username in database:
        friend = input("Which friend do you want to remove? ")
        if friend in database[username]["Friends"]:
            database[username]["Friends"].remove(friend)
        else:
            return(False)
    else:
        return(False)
def delete_account():
    username = input("What do you want to delete? ")
    if username in database:
        database.pop(username)
        print("True")
    else:
        return(False)
def quit():
    print("True")
    print(database)
    exit()
def main():
    while True:
        menu.displaymenu()
        option = menu.getoption()
        if option == 1:
            register()
        elif option == 2:
            printlogin = login()
            print(printlogin)
        elif option == 3:
            leaderboard()
        elif option == 4:
            add_friend()
        elif option == 5:
            remove_friend()
        elif option == 6:
            delete_account()
        elif option == 7:
            quit()
        else:
            print("Not a valid option")

main()