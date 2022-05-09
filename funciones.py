import json
import requests
import os
import urllib
from urllib import request

def juegos_obtiene(key,id):
    juegos=[]
    r=requests.get(f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={key}&include_played_free_games=1&include_appinfo=True&steamid={id}&format=json")
    datos = r.json()
    for i in datos.get("response").get("games"):
        juegos.append(i.get("name"))
    return juegos