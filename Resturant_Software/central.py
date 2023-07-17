from table import Table
from manager import Manager
from group import Group
menu = {"hamburger":2, "cheeseburger":2.50, "fries":1, "drink":1, "avacado_toast":15, "starbucks_coffee":100}
table1 = Table(seats = 3, high_chairs = 1)
manager1 = Manager()
group1 = Group(3,1)

#Homework: Caculate spending and get a free table (Do one)
print(group1.caculate_spendings(menu))