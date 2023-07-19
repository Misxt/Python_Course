options = {1:"Add a table", 2:"Seat a group", 3:"Free a table", 4:"Show total earnings", 5:"Remove a table", 6:"Quit"}
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