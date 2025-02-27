# Description:
# Created by Emilia on 2025-02-27

class Game:
    '''yap herre'''
    id: int
    name: str
    genre: list[str]
    description: str
    requirements: list[str]

    def __init__(self, id, name, genre, description, requirements):
        self.id = id
        self.name = name
        self.genre = genre
        self.description = description
        self.requirements = requirements

    def __str__(self):
        return f'game: {self.name}, id: {self.id}, genres: {self.genre}'

