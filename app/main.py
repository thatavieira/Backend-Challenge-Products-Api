from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"Challenge": "Backend Products Api"}
