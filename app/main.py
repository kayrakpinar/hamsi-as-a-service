from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os
import random

cwd = os.getcwd()
arr = os.listdir(cwd + "/static/hamsi")

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    foto = random.choice(arr)
    data = {    
    "resim": "/hamsi/{}".format(foto)
    }
    return templates.TemplateResponse("index.html", {"request": request, "data": data})

@app.get("/gizli", response_class=HTMLResponse)
async def home(request: Request):
    data = {    
    "mesaj": "burda ne arıyorsun acaba"
    }
    return templates.TemplateResponse("gizli.html", {"request": request, "data": data})