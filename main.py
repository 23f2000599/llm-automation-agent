from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Request model
class TaskRequest(BaseModel):
    task: str

# Dummy /run endpoint
@app.post("/run")
async def run_task(request: TaskRequest):
    return {"message": f"Executing: {request.task}"}

# Dummy /read endpoint
@app.get("/read")
async def read_data(path: str):
    return {"data": f"Reading file: {path}"}

