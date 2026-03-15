# Viperr Visuals Backend

## Deploy на Railway:
1. Зайди на https://railway.app
2. New Project → Deploy from GitHub repo
3. Загрузи эти файлы в GitHub репозиторий
4. Railway сам задеплоит, даст URL типа: https://viperr-backend.up.railway.app

## Endpoints:
- POST /ping  — {"player": "NickName", "server": "play.funtime.su"}
- GET /players?server=play.funtime.su — возвращает список игроков с Viperr Visuals
