from table import Table
from manager import Manager
from group import Group
menu = {"hamburger":2, "cheeseburger":2.50, "fries":1, "drink":1, "avacado_toast":15, "starbucks_coffee":100}
table1 = Table(seats = 4, high_chairs = 2, table_number = 1)
table2 = Table(seats = 3, high_chairs = 1, table_number = 2)
manager1 = Manager()
group1 = Group(3,1)
manager1.add_table(table1)
manager1.add_table(table2)
print(manager1.receive_group(group1, menu))
print(manager1.earnings)