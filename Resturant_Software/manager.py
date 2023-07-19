class Manager:
    def __init__(self) -> None:
        self.earnings = 0
        self.tables = []

    def add_table(self, table):
        self.tables.append(table)

    def remove_table(self, tablenumber):
        for i in range(len(self.tables)):
            if self.tables[i].table_number == tablenumber:
                self.tables.pop(i)
                break

    def get_free_table(self, group):
        """
        Picks a free table to be considered for seating (Depending on the number of adults and children)
        """
        best_table = None
        for i in range(len(self.tables)):
            if self.tables[i].occupied == False:
                if group.number_of_adults <= self.tables[i].seats and group.number_of_children <= self.tables[i].high_chairs and best_table == None:
                        best_table = self.tables[i]
                elif best_table is not None:
                    if self.tables[i].seats - group.number_of_adults < best_table.seats - group.number_of_adults:
                        if self.tables[i].seats - group.number_of_adults >= 0:
                            if self.tables[i].high_chairs - group.number_of_children < best_table.high_chairs - group.number_of_children:
                                if self.tables[i].high_chairs - group.number_of_children >= 0:
                                    best_table = self.tables[i]
        return best_table
    
    def free_table(self, tablenumber):
        for i in range(len(self.tables)):
            if self.tables[i].table_number == tablenumber:
                self.tables[i].occupied = False
    
    def receive_group(self, group, menu) -> int:
        """
        Step one: Check if there is a free table or not
        Step two: If we have a table, change that table to occupied
        Step three: Caculate the spending of the group
        Step four: Return the table number, if you don't have a free table, return -1
        """
        free_table = self.get_free_table(group)
        if free_table is not None:
            free_table.occupied = True
            self.earnings = self.earnings + group.caculate_spendings(menu)
            return free_table.table_number
        return -1

        