from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from hindsight_client import Hindsight
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

client = Hindsight(
    base_url="https://api.hindsight.vectorize.io",
    api_key=os.getenv("HINDSIGHT_API_KEY")
)

BANK_ID = "buildbuddy"


class ChatRequest(BaseModel):
    message: str


class RememberRequest(BaseModel):
    memory: str


class SearchRequest(BaseModel):
    query: str


@app.get("/")
def home():
    return FileResponse("index.html")


@app.get("/memories")
async def memories():

    result = await client.arecall(
        bank_id=BANK_ID,
        query="What are the important facts, decisions, preferences, technologies, and solutions in this project?"
    )

    memory_list = []

    for item in result.results:
        memory_list.append(item.text)

    return {
        "memories": memory_list,
        "count": len(memory_list)
    }


@app.post("/search-memory")
async def search_memory(request: SearchRequest):

    result = await client.arecall(
        bank_id=BANK_ID,
        query=request.query
    )

    memory_list = []

    for item in result.results:
        memory_list.append(item.text)

    return {
        "memories": memory_list,
        "count": len(memory_list)
    }


@app.post("/remember")
async def remember(request: RememberRequest):

    await client.aretain(
        bank_id=BANK_ID,
        content=f"Important project memory: {request.memory}"
    )

    return {
        "message": "Memory saved successfully!"
    }


@app.post("/chat")
async def chat(request: ChatRequest):

    await client.aretain(
        bank_id=BANK_ID,
        content=f"Developer said: {request.message}"
    )

    response = await client.areflect(
        bank_id=BANK_ID,
        query=request.message
    )

    return {
        "answer": response.text,
        "memory_used": True
    }