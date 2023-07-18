import random
class Group:
    def __init__(self, number_of_adults:int, number_of_children:int) -> None:
        self.number_of_adults = number_of_adults
        self.number_of_children = number_of_children

    def caculate_spendings(self, menu) -> float:
        """
        Randomly selects items from the menu and returns the total spending
        """
        total_price = 0
        for i in range(self.number_of_adults):
            menuoptions = list(menu.keys())
            orderitem = random.choice(menuoptions)
            total_price = menu[orderitem] + total_price
        return total_price
        