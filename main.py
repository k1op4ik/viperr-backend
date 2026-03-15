from fastapi import FastAPI
from pydantic import BaseModel
import time, threading

app = FastAPI()

online: dict[str, float] = {}
TIMEOUT = 120

class PlayerPing(BaseModel):
    player: str
    server: str

@app.post("/ping")
def ping(data: PlayerPing):
    key = f"{data.server.lower()}:{data.player.lower()}"
    online[key] = time.time()
    return {"ok": True}

@app.get("/players")
def get_players(server: str):
    now = time.time()
    result = []
    for key, ts in list(online.items()):
        if now - ts > TIMEOUT:
            del online[key]
            continue
        srv, player = key.split(":", 1)
        if srv == server.lower():
            result.append(player)
    return {"players": result}

def cleanup():
    while True:
        now = time.time()
        for key in list(online.keys()):
            if now - online[key] > TIMEOUT:
                del online[key]
        time.sleep(30)

threading.Thread(target=cleanup, daemon=True).start()
