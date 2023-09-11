import random
"""
Merge the two previous files
Create a crud application to store youtube video's data
Add a new key with ID
Optional: Create an extra endpoint to do something (Like get all videos by certian creators)
"""
#Run command: uvicorn youtube_crud:app --reload
from fastapi import FastAPI, status, HTTPException

app = FastAPI()

class Video:
    def __init__(self, name, duration, owner) -> None:
        self.name = name
        self.duration = duration
        self.owner = owner

class VideosDataBase:
    def __init__(self) -> None:
        self.videos = {}

    def create(self, name, duration, owner):
        id = random.randint(0, 10000)
        self.videos[id] = Video(name, duration, owner)
        return id

    def read(self, id):
        if id not in self.videos:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Video {id} not found")
        return self.videos[id]
        
    def update(self, id, name, duration, owner):
        if id not in self.videos:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Video {id} not found")
        self.videos[id] = Video(name, duration, owner)

    def delete(self, id):
        if id not in self.videos:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Video {id} not found")
        self.videos.pop(id)


videos_database = VideosDataBase()
videos_database.create("Me at the zoo", 2, "Asa")
videos_database.create("Test", 99, "Luciano")

@app.post("/video", status_code=status.HTTP_201_CREATED)
def create_user(name:str, duration:float, owner:str):
    id = videos_database.create(name, duration, owner)
    return id

@app.get("/video/{id}", status_code=status.HTTP_200_OK)
def get_user(id:int):
    return videos_database.read(id)

@app.put("/user/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_user(id:int, name:str, duration:float, owner:str):
    videos_database.update(id, name, duration, owner)

@app.delete("/user/{id}", status_code=status.HTTP_202_ACCEPTED)
def delete_user(id:int):
    videos_database.delete(id)
    
#adasedwqqdasdqwwasqFastAP