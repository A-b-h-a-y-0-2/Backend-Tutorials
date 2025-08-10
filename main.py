from fastapi import FastAPI
from fastapi.params import Body
from typing import Dict
app = FastAPI()

@app.get("/content")
async def display_content():
    return {'message': 'hello Darkness my old friend'}

@app.post("/send_post")
async def send_posts(payload:Dict = Body(...)):
    # print(payload)
    return {"message": "Post created successfully", "data": {"title": payload['title'], "content": payload['names']}}
