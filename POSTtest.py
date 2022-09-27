import json
from tkinter import Y
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class NIMMHS(BaseModel):
    NIM: str
    Nama: str

x = None

@app.post("/datamhs/", response_model=NIMMHS)
async def store_datamhs(data: NIMMHS):
    x = json.loads(data)
    return x