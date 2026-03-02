from fastapi import FastAPI
from pydantic import BaseModel
from app.router import route_query

app = FastAPI(
    title="Smart LLM Router API",
    description="Adaptive Multi-Model Routing System",
    version="1.0"
)

class QueryRequest(BaseModel):
    query: str


@app.get("/")
def root():
    return {"message": "Smart LLM Router is running"}


@app.post("/ask")
def ask_question(request: QueryRequest):
    result = route_query(request.query)
    return result