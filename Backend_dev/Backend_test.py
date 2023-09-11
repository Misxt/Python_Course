#Run command: uvicorn Backend_test:app --reload
from fastapi import FastAPI

app = FastAPI()

database = [
    {
        "title":"I Went to Space", 
        "duration":9,
        "owner":"MrBeast"
    },
    {
        "title":"I Went to Space", 
        "duration":9,
        "owner":"MrBeast"
    },
    {
        "title":"I Went to Space", 
        "duration":9,
        "owner":"MrBeast"
    }
]

@app.get("/number")
def get_number():
    return number

@app.post("/number")
def post_number(new_number: int):
    global number
    number = new_number

#adasedwqqdasdqwwasq