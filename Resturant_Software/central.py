from table import Table
from manager import Manager
from group import Group
import resturant_options
menu = {"hamburger":2, "cheeseburger":2.50, "fries":1, "drink":1, "avacado_toast":15, "starbucks_coffee":100}
manager1 = Manager()
def main():
    while True:
        resturant_options.displaymenu()
        option = resturant_options.getoption()
        if option == 1:
            seats = int(input("How many seats are at this table? "))
            high_chairs = int(input("How many high chairs are at this table? "))
            table1 = Table(seats, high_chairs)
            manager1.add_table(table1)
        elif option == 2:
            adults = int(input("How many adults are in this group? "))
            children = int(input("How many children are in this group? "))
            group1 = Group(adults, children)
            seated_table_number = manager1.receive_group(group1, menu)
            if seated_table_number != -1:
                print(f"Please take a seat at table {seated_table_number}")
            else:
                print("Sorry, the restrurant is too full at the moment")
        elif option == 3:
            table_free = int(input("Which table number do you want to free? "))
            manager1.free_table(table_free)
        elif option == 4:
            print(manager1.earnings)
        elif option == 5:
            tableremove = int(input("Which table do you want to remove? "))
            manager1.remove_table(tableremove)
        elif option == 6:
            break
        else:
            print("Not a valid option")
if __name__ == "__main__":
    main()
#Homework: Read and understand the minecraft menu