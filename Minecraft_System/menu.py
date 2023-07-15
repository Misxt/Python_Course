options = {1:"Register", 2:"Login", 3:"Leaderboard", 4:"Add Friend", 5:"Remove friend", 6:"Delete account", 7:"Quit"}
def displaymenu():
    print("-----------------")
    for key in options:
        print(key, options[key])
def getoption():
    e = input("Choose a number: ")
    if e.isnumeric():
        e = int(e)
        if e in options:
            return(e)
        else:
            print("Invalid Number!")
            return(getoption())
    else:
        print("Input a Number!")
        return(getoption())


