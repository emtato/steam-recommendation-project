# Description:
# Created by Emilia on 2025-02-27
from typing import Any

class Game:
    '''yap herre'''
    id: int
    name: str
    price: dict[str:Any]
    description: str
    languages: str
    image: str
    requirements: dict[str: str]
    developers: list[str]
    platforms: dict[str: bool]
    categories: list[str]
    genres: list[str]
    dlc: bool

    def __init__(self, id: int, name: str, price: int, description: str, languages: str, image: str,
            requirements: dict[str: str], developers: list[str], platforms: dict[str: bool], categories: list[str],
            genres: list[str], dlc):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.languages = languages
        self.image = image
        self.requirements = requirements
        self.developers = developers
        self.platforms = platforms
        self.categories = categories
        self.genres = genres
        self.dlc = dlc

    def __repr__(self):
        return f"Game(id={self.id}, name='{self.name}', price={self.price}, genre={self.genres})"
