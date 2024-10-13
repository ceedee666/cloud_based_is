from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/auth")
async def auth(code: str):
    print(code)
    return "OK"
