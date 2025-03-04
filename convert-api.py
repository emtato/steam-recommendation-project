# Description: converts the api data to csv file, this file does not need to be run more than once on the full data file
# Created by Emilia on 2025-02-27
import json
from objects import Game
import requests

apps = 'http://api.steampowered.com/ISteamApps/GetAppList/v0002/?key=STEAMKEY&format=json'


def get_ids(start: int, end: int) -> list[int]:
    response = requests.get(apps)
    if response.status_code == 200:
        data = response.json()

        data = data["applist"]["apps"]
        appcount = len(data)
        return [data[i]['appid'] for i in range(start, min(appcount, end))]

    else:
        print(f"Error: {response.status_code}")


appinfo = 'https://store.steampowered.com/api/appdetails?appids='

import re


def strip_html(raw_html):
    """
    Remove HTML tags and extra whitespace from a string.
    """
    if not raw_html:
        return ""
    # Remove HTML tags using a regex
    text = re.sub(r'<[^>]+>', '', raw_html)
    # Collapse multiple spaces/newlines into one space and trim
    return " ".join(text.split())


def get_clean_requirements(req):
    """
    Accepts a requirement entry which may be a dict, list, or string,
    and returns a cleaned, plain-text version.
    """
    if isinstance(req, dict):
        # Assume we want the "minimum" key if it exists.
        return strip_html(req.get("minimum", ""))
    elif isinstance(req, list):
        # Join any string entries from the list.
        return " ".join(strip_html(item) for item in req if isinstance(item, str))
    elif isinstance(req, str):
        return strip_html(req)
    return ""


def get_deets(games: list[int]) -> list[Game]:
    appinfo = "https://store.steampowered.com/api/appdetails?appids="
    game_list = []

    for game in games:
        response = requests.get(appinfo + str(game))
        data = response.json()
        print(data)

        if data is not None and str(game) in data and 'data' in data[str(game)] and data[str(game)]['success']:
            data_dict = data[str(game)]['data']

            # Extract name
            name = data_dict.get("name", "Unknown")

            # Extract freeness
            price = data_dict.get("price_overview", "unknown")

            # Extract lingo
            languages = data_dict.get("supported_languages", "Unknown")

            # Extract image
            image = data_dict.get("capsule_image", "unknown")

            # Extract code monkeys
            developers = data_dict.get("developers", "unknown")

            # Extract operating systems (>> windows)
            platforms = data_dict.get("platforms", "unknown")

            # Extract categories
            categories = [cat['description'] for cat in data_dict.get('genres', [])]

            # Extract genres
            genres = [genre_dict['description'] for genre_dict in data_dict.get('genres', [])]

            # Extract description
            description = data_dict.get("short_description", "No description available.")

            # Extract system requirements
            requirements = {'PC': get_clean_requirements(data_dict.get('pc_requirements')),
                            'Mac': get_clean_requirements(data_dict.get('mac_requirements')),
                            'Linux': get_clean_requirements(data_dict.get('linux_requirements'))}

            # Append to game list
            game_list.append(
                Game(game, name, price, description, languages, image, requirements, developers, platforms, categories,
                     genres))

    return game_list


def write_to_csv(games: list[Game]) -> None:
    with open("data.csv", "a") as file:
        for game in games:
            file.write(
                f"{game.id},'{game.name}',\"{game.price}\",\"[{game.description}]\",\"{game.languages}\",{game.image},\"{game.requirements}\",\"{game.developers}\",\"{game.platforms}\",\"{game.categories}\",\"{game.genres}\"\n")



write_to_csv(get_deets(get_ids(74, 100)))
