from fastapi import FastAPI

from app.api import analyze

app = FastAPI()

app.include_router(analyze.router)


@app.get("/", tags=["Logs"])
async def read_root():
    return {"message": "Successful!"}
