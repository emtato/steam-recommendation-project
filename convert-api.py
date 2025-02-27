# Description: converts the api data to csv file, this file does not need to be run more than once on the full data file
# Created by Emilia on 2025-02-27
import json
from objects import Game
import requests

apps = 'http://api.steampowered.com/ISteamApps/GetAppList/v0002/?key=STEAMKEY&format=json'


def get_ids(length: int) -> list[int]:
    response = requests.get(apps)
    if response.status_code == 200:
        data = response.json()

        data = data["applist"]["apps"]
        appcount = len(data)
        return [data[i]['appid'] for i in range(appcount - length, appcount)]

    else:
        print(f"Error: {response.status_code}")


appinfo = 'https://store.steampowered.com/api/appdetails?appids='


def get_deets(games: list[int]) -> list[Game]:
    appinfo = "https://store.steampowered.com/api/appdetails?appids="
    game_list = []

    for game in games:
        response = requests.get(appinfo + str(game))
        data = response.json()
        print(data)

        if str(game) in data and 'data' in data[str(game)] and data[str(game)]['success']:
            data_dict = data[str(game)]['data']

            # Extract name
            name = data_dict.get("name", "Unknown")

            # Extract genres
            genres = [genre_dict['description'] for genre_dict in data_dict.get('genres', [])]

            # Extract description
            description = data_dict.get("short_description", "No description available.")

            # Extract system requirements
            requirements = {"PC": data_dict.get("pc_requirements").get("minimum"),
                "Mac": data_dict.get("mac_requirements"),
                "Linux": data_dict.get("linux_requirements")}

            # Append to game list
            game_list.append(Game(game, name, genres, description, requirements))

    return game_list


def write_to_csv(games: list[Game]) -> None:
    with open("data.csv", "a") as file:
        for game in games:
            genres = str(game.genre)
            genres_without_commas = ""
            for char in genres:
                genres_without_commas += char if char != ',' else ''

            requirements_without_commas = ""
            for char in str(game.requirements):
                requirements_without_commas +=  char if char != ',' else ''

            file.write(f"{game.id},{game.name},[{genres_without_commas}],{game.description},{requirements_without_commas}\n")


write_to_csv(get_deets(get_ids(4)))
