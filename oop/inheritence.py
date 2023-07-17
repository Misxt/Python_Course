import random
class Cloud:
    def __init__(self, name:str, amount_of_clouds:int) -> None:
        self.amount_of_clouds = random.radnint(0,10)

    def how_many_clouds(self, amount_of_clouds):
        print(self.amount_of_clouds)

class Sky:
    def __init__(self, amount_of_clouds:int) -> None:
        self.clouds = []
        for i in range (amount_of_clouds):
            self.clouds.append(Cloud)

    def sundial(self):
        print(random.randint(0,24))




