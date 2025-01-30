from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from sys import platform
from typing import Dict, Any
import os
from uuid import uuid4

upper_bound = 1.21
boundary = 5.8
lower_bound = -0.2

app = FastAPI()

video_dir = 'videos'

@app.post('/video')
def video(payload: Dict[Any, Any]):
    name = payload['name']
    # get video path
    video_path = name
    return FileResponse(video_path)

@app.post('/verify')
def verify(payload: Dict[Any, Any]):
    currentTime = payload['currentTime']
    if currentTime > boundary + lower_bound and currentTime < boundary + upper_bound:
        return {'msg': 1}
    else:
        return {'msg': 0}

app.mount('/video', StaticFiles(directory=video_dir))

app.mount('/', StaticFiles(directory='frontend/dist', html=True))


if __name__ == '__main__':
    # uvicorn.run(app, port=7777)
    if platform == 'darwin':
        uvicorn.run("main:app", port=7777, reload=True)
    elif platform == 'linux' or platform == 'linux2':
        uvicorn.run("main:app", host="0.0.0.0", port=7777)