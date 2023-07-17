class Manager:
    def __init__(self) -> None:
        self.earnings = 0
        self.tables = []

    def add_table(self, table):
        self.tables.append(table)

    def get_free_table(self, group):
        """
        Picks a free table to be considered for seating (Depending on the number of adults and children)
        """
        pass