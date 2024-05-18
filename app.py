from fastapi import FastAPI

import src

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

