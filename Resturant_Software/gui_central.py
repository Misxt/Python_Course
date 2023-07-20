from tkinter import *
from group import Group
from table import Table
from manager import Manager
from central import menu
manager1 = Manager()
window = Tk()
# window.configure(bg = "#6c5b7b")
window.title("Resturant Manager") #This is the title of the window, or what appears on top
window.geometry('1550x850')#Setting the window size
x = 0
y = 0
buttons_map = {}#The keys should be the table number (Intergers) and the values should be the buttons (tk.button)
unified_font = ("quicksand", 18)
#Creating entries
number_of_adults = IntVar()
chairs_entry = Entry(textvariable = number_of_adults, font = unified_font)
chairs_entry.grid(column = 5, row = 0, padx = 20, pady = 20)

number_of_children = IntVar()
high_chairs_entry = Entry(textvariable = number_of_children, font = unified_font)
high_chairs_entry.grid(column = 5, row = 1, padx = 20, pady = 20)

#Creating static labels
lbl = Label(window, text = "# of Adults/Chairs: ", font = unified_font)
lbl.grid(column = 4, row = 0, padx = 20, pady = 20)

lbl = Label(window, text = "# of Children/High Chairs: ", font = unified_font)
lbl.grid(column = 4, row = 1, padx = 20, pady = 20)

#Creating the label that will change
actv_lbl = Label(window, text = "Waiting for group", font = unified_font)
actv_lbl.grid(column = 4, row = 3, padx = 20, pady = 20)

def recive_group():
    group1 = Group(number_of_adults.get(), number_of_children.get())
    seated_table_number = manager1.receive_group(group1, menu)
    if seated_table_number != -1:
        actv_lbl.config(text = f"Please take a seat at table {seated_table_number}")
        button = buttons_map[seated_table_number]
        button_pressed(button, seated_table_number)
    else:
        actv_lbl.config(text = "Sorry, we are too full at the moment")

#Creating buttons
btn = Button(window, text = "Receive Group", command = recive_group, font = unified_font, width = 10, height = 5, padx = 20, pady = 20, bg = "#355c7d", activebackground = "#6c5b7b")
btn.grid(column = 4, row = 2)

def button_pressed(button_context, table_number):
    color = button_context["bg"]
    if color == "#355c7d":
        color = "red"
    else:
        color = "#355c7d"
        manager1.free_table(table_number)
    button_context.config(bg = color)

def add_table():
    global x
    global y
    table1 = Table(number_of_adults.get(), number_of_children.get())
    manager1.add_table(table1)
    table_number = table1.table_number
    btn = Button(window, text = f"Table {table_number}", font = unified_font, width = 10, height = 5, padx = 20, pady = 20, bg = "#355c7d", activebackground = "#6c5b7b")
    btn.config(command = lambda b = btn, n = table_number: button_pressed(b, n))
    buttons_map[table_number] = btn
    btn.grid(column=x, row=y)
    if x >= 3:
        x = 0
        y = y + 1
    else:
        x = x + 1

tbl_btn = Button(window, text = "Add Table", command = add_table, font = unified_font, width = 10, height = 5, padx = 20, pady = 20, bg = "#355c7d", activebackground = "#6c5b7b")
tbl_btn.grid(column = 5, row = 2)


window.mainloop()