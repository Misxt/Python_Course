class Table:
    quantity = 0
    def __init__(self, seats, high_chairs) -> None:
        self.seats = seats
        self.high_chairs = high_chairs
        self.occupied = False
        Table.quantity = Table.quantity + 1
        self.table_number = Table.quantity