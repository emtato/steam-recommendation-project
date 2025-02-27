# Description: converts the api data to csv file, this file does not need to be run more than once on the full data file
# Created by Emilia on 2025-02-27

def get_ids(filename: str) -> list[int]:
    with open(filename) as file:

        for game in file:
            id = game[0]
            return [game[0]['appid']]
