from fastapi import FastAPI
import requests

app = FastAPI()

# 🔹 Page d'accueil
@app.get("/")
def home():
    return {
        "message": "🚴 Tour de France API en ligne !",
        "routes": ["/riders", "/teams", "/stages", "/classement", "/live"]
    }

# 🔹 Riders (FAKE pour l'instant)
@app.get("/riders")
def riders():
    return {
        "riders": [
            {"name": "Jonas Vingegaard", "team": "Visma"},
            {"name": "Tadej Pogacar", "team": "UAE"},
            {"name": "Remco Evenepoel", "team": "Soudal"}
        ]
    }

# 🔹 Teams
@app.get("/teams")
def teams():
    return {
        "teams": [
            "UAE Team Emirates",
            "Visma | Lease a Bike",
            "Soudal Quick-Step",
            "INEOS Grenadiers"
        ]
    }

# 🔹 Stages
@app.get("/stages")
def stages():
    return {
        "stages": [
            "Étape 1 - Sprint",
            "Étape 2 - Montagne",
            "Étape 3 - Contre-la-montre"
        ]
    }

# 🔹 Classement (exemple)
@app.get("/classement")
def classement():
    return {
        "classement_general": [
            {"position": 1, "name": "Pogacar"},
            {"position": 2, "name": "Vingegaard"},
            {"position": 3, "name": "Evenepoel"}
        ]
    }

# 🔹 Live (simulation)
@app.get("/live")
def live():
    return {
        "status": "En course 🚴",
        "leader": "Pogacar",
        "km_restants": 42
    }
