class Table:
    def __init__(self, seats, high_chairs) -> None:
        self.seats = seats
        self.high_chairs = high_chairs
        self.occupied = False