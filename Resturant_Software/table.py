class Table:
    def __init__(self, seats, high_chairs, table_number) -> None:
        self.seats = seats
        self.high_chairs = high_chairs
        self.occupied = False
        self.table_number = table_number