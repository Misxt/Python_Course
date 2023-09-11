#Run command: uvicorn Backend_test:app --reload
from fastapi import FastAPI

app = FastAPI()

class LevelsDataBase:
    def __init__(self) -> None:
        self.levels = {}

    def create(self, name, levels):
        self.levels[name] = levels

    def read(self, name):
        return self.levels[name]
        
    def update(self, name, levels):
        self.levels[name] = levels

    def delete(self, name):
        self.levels.pop(name)

    def all_levels(self, cutoff):
        return_list = []
        for keys in self.levels:
            if self.levels[keys] > cutoff:
                return_list.append(keys)
        return return_list


my_database = LevelsDataBase()
my_database.create("Asa", 6)
my_database.create("Luciano", 5.9)

@app.post("/user")
def create_user(username:str, level:float):
    my_database.create(username, level)
    return "User created succesfully"

@app.get("/user/{username}")
def get_user(username:str):
    return my_database.read(username)

@app.put("/user")
def update_user(username:str, level:float):
    my_database.update(username, level)
    return "Update successful"

@app.delete("/user")
def delete_user(username:str):
    my_database.delete(username)
    return "User deleted"
    
@app.post("/user/addone")
def addone(username:str):
    current_level = my_database.read(username)
    my_database.update(username, current_level + 1)
    return "Added successfully"

@app.get("/user/by/greater")
def get_users_by_greater(cutoff:float):
    return my_database.all_levels(cutoff)
#adasedwqqdasdqwwasq