from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

# 🔹 HOME
@app.get("/")
def home():
    return {
        "message": "🚴 Tour de France SCRAPER",
        "routes": [
            "/classement",
            "/stages",
            "/riders"
        ]
    }

# 🔥 CLASSEMENT GÉNÉRAL
@app.get("/classement")
def classement():
    url = "https://www.letour.fr/fr/classement-general"
    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.text, "html.parser")

    data = []

    rows = soup.select(".rankingTable__row")

    for row in rows[:10]:
        try:
            name = row.select_one(".rider-name").text.strip()
            team = row.select_one(".team").text.strip()
            position = row.select_one(".position").text.strip()

            data.append({
                "position": position,
                "name": name,
                "team": team
            })
        except:
            continue

    return {"top10": data}

# 🔥 ÉTAPES
@app.get("/stages")
def stages():
    url = "https://www.letour.fr/fr/etapes"
    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.text, "html.parser")

    data = []

    stages = soup.select(".stage")

    for stage in stages[:10]:
        try:
            title = stage.select_one(".stage-title").text.strip()
            date = stage.select_one(".stage-date").text.strip()

            data.append({
                "title": title,
                "date": date
            })
        except:
            continue

    return {"stages": data}

# 🔥 COUREURS
@app.get("/riders")
def riders():
    url = "https://www.letour.fr/fr/coureurs"
    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.text, "html.parser")

    data = []

    riders = soup.select(".rider")

    for rider in riders[:20]:
        try:
            name = rider.select_one(".rider-name").text.strip()
            team = rider.select_one(".team-name").text.strip()

            data.append({
                "name": name,
                "team": team
            })
        except:
            continue

    return {"riders": data}
