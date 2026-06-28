from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API Tour de France OK 🚴"}

@app.get("/cyclisme")
def cyclisme():
    return {"sport": "cyclisme", "event": "Tour de France"}

@app.get("/classement")
def classement():
    data = [
        {"nom": "Vingegaard", "temps": "00:00:00"},
        {"nom": "Pogacar", "temps": "+00:10"},
    ]
    return {"classement": data}

@app.get("/live")
def live():
    return {"status": "course en direct 🔴"}