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

def ultimo_juego(key,id,juego):
    horas=[]
    r=requests.get(f"https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key={key}&steamid={id}&format=json")
    datos = r.json()
    for i in datos.get("response").get("games"):
        if i.get("name") == juego:
            horas.append(i.get("playtime_forever"))
    return horas

def info_user(key,id):
    info=[]
    r=requests.get(f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={key}&steamids={id}")
    datos = r.json()
    for i in datos.get("response").get("players"):
        info.append(i.get("steamid"))
        info.append(i.get("realname"))
        info.append(i.get("loccountrycode"))
    return info


