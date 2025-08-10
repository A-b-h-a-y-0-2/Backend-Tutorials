from fastapi import FastAPI
from fastapi.params import Body
from typing import Optional
from pydantic import BaseModel

class Posts(BaseModel):
    title:str
    content:str
    names: Optional[str] = None
    published: bool = True
app = FastAPI()

@app.get("/content")
async def display_content():
    return {'message': 'hello Darkness my old friend'}

@app.post("/send_post")
async def send_posts(new_post: Posts):
    print(new_post.model_dump())
    
    return {"message": "Post received successfully", "post": new_post}
    # print(payload)
