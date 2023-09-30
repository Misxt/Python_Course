import random
"""
Merge the two previous files
Create a crud application to store youtube video's data
Add a new key with ID
Optional: Create an extra endpoint to do something (Like get all videos by certian creators)
"""
#Run command: uvicorn youtube_crud:app --reload
from fastapi import FastAPI, status, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI()

class Video:
    def __init__(self, name, duration, owner) -> None:
        self.name = name
        self.duration = duration
        self.owner = owner
    
    def to_dictionary(self):
        dictionary = {"name":self.name, "duration":self.duration, "owner":self.owner}
        return dictionary

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

    def all_owner_videos(self, owner):
        return_list = []
        for id in self.videos:
            if self.videos[id].owner == owner:
                return_list.append(self.videos[id])
        return return_list



videos_database = VideosDataBase()
videos_database.create("Me at the zoo", 2, "Asa")
videos_database.create("Test", 99, "Luciano")

@app.post("/video", status_code=status.HTTP_201_CREATED)
def create_video(name:str, duration:float, owner:str):
    id = videos_database.create(name, duration, owner)
    return id

@app.get("/video/{id}", status_code=status.HTTP_200_OK)
def get_video(id:int):
    return videos_database.read(id)

@app.put("/video/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_video(id:int, name:str, duration:float, owner:str):
    videos_database.update(id, name, duration, owner)

@app.delete("/video/{id}", status_code=status.HTTP_202_ACCEPTED)
def delete_video(id:int):
    videos_database.delete(id)

@app.get("/video/owner/{owner}", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
def all_vids_by_owner(owner: str):
    data = videos_database.all_owner_videos(owner)
    
    # Convert JSON data to an HTML table with CSS styling
    table_html = """
    <style>
        table {
            border-collapse: collapse;
            width: 80%;
            margin: 20px auto;
        }
        th, td {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
    <table>
        <tr>
            <th>Name</th>
            <th>Duration</th>
            <th>Owner</th>
        </tr>
    """

    for item in data:
        table_html += f"""
        <tr>
            <td>{item.name}</td>
            <td>{item.duration}</td>
            <td>{item.owner}</td>
        </tr>
        """

    table_html += "</table>"

    # Embed the HTML table into your response
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Video List</title>
    </head>
    <body>
        <h1>Videos by Owner: {owner}</h1>
        {table_html}
    </body>
    </html>
    """

@app.get("/", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    
#adasedwqqdasdqwwasqFastAP