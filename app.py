from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.model import Model
from src.prompts import PromptTemplate
from src.configs import ModelConfigs


def init():
    global model

    model = Model(
        prompt_template=PromptTemplate(),
        model_configs=ModelConfigs
    )

init()

app = FastAPI()

@app.get("/ping")
async def ping():
    return {"response": "Hello World!"}

@app.get("/translate/{text}")
async def translate(text: str):
    try:
        translation = model.generate(text)
        return {"output": translation}
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})