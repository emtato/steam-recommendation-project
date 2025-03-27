# Description:
# Created by Emilia on 2025-03-23
from __future__ import annotations

import ast
import csv
from typing import Any, Union

from attr import dataclass

from typing import Any

# weight of each category for determining matches
# we can create a simple ranking system where the user ranks whats most important to them for personalization
genre, languages, platforms = 0, 0, 0


@dataclass
class Game:
    '''yap herre'''
    id: int
    name: str
    price: dict[str:Any]
    description: str
    languages: list[str]
    image: str
    requirements: dict[str: str]
    developers: list[str]
    platforms: dict[str: bool]
    categories: list[str]
    genres: list[str]
    dlc: bool


class _Vertex:
    """A vertex in a graph.

    Instance Attributes:
        - item: The data stored in this vertex.
        - neighbours: The vertices that are adjacent to this vertex.

    Representation Invariants:
        - self not in self.neighbours
        - all(self in u.neighbours for u in self.neighbours)
    """

    item: Any
    neighbours: dict[_Vertex, Union[int, float]]

    def __init__(self, item: Any, neighbours: set[_Vertex]) -> None:
        """Initialize a new vertex with the given item and neighbours."""
        self.item = item
        self.neighbours = neighbours

    def check_connected(self, target_item: Any, visited: set[_Vertex]) -> bool:
        """Return whether this vertex is connected to a vertex corresponding to the target_item,
        WITHOUT using any of the vertices in visited.

        Preconditions:
            - self not in visited
        """
        if self.item == target_item:
            return True
        else:
            visited.add(self)
            for u in self.neighbours:
                if u not in visited:
                    if u.check_connected(target_item, visited):
                        return True

            return False


class Graph:
    """A graph.

    Representation Invariants:
        - all(item == self._vertices[item].item for item in self._vertices)
    """
    # Private Instance Attributes:
    #     - _vertices:
    #         A collection of the vertices contained in this graph.
    #         Maps item to _Vertex object.
    _vertices: dict[Any, _Vertex]

    def __init__(self) -> None:
        """Initialize an empty graph (no vertices or edges)."""
        self._vertices = {}

    def add_vertex(self, item: Any) -> None:
        """Add a vertex with the given item to this graph.

        The new vertex is not adjacent to any other vertices.

        Preconditions:
            - item.id not in self._vertices
        """
        if item.id not in self._vertices:
            self._vertices[item.id] = _Vertex(item, set())

    def add_edge(self, item1: Any, item2: Any, weight: Union[int, float]) -> None:
        """Add an edge between the two vertices with the given items in this graph,
        with the given weight.

        Raise a ValueError if item1 or item2 do not appear as vertices in this graph.

        Preconditions:
            - item1 != item2
        """
        if item1 in self._vertices and item2 in self._vertices:
            v1 = self._vertices[item1]
            v2 = self._vertices[item2]

            # Add the new edge
            v1.neighbours[v2] = weight
            v2.neighbours[v1] = weight
        else:
            # We didn't find an existing vertex for both items.
            raise ValueError

    def get_weight(self, item1: Any, item2: Any) -> Union[int, float]:
        """Return the weight of the edge between the given items.

        Return 0 if item1 and item2 are not adjacent.

        Preconditions:
            - item1 and item2 are vertices in this graph
        """
        v1 = self._vertices[item1]
        v2 = self._vertices[item2]
        return v1.neighbours.get(v2, 0)

    def get_vertex(self, item: Any):
        """
        Returns the vertex given a corresponding item.
        """
        return self._vertices[item]

    def build_graph(self, data_file: str, amount: int) -> Graph:
        # Here we are using the 'encoding=' to make sure everyone's computer will be able to use the csv file
        with open(data_file, 'r', encoding='utf8') as file:
            reader = csv.reader(file)
            row = next(reader)
            row = 'useless'
            row = ':('

            dic = {}
            for i, row in enumerate(reader):
                # print(row)
                if i >= amount - 1:
                    break
                if len(row) != 12:
                    print(i, row[0])
                    print("NOOOO")
                try:
                    (
                        id, name, price_overview, description, supported_languages, capsule_image, requirements,
                        developers,
                        platforms, categories, genres, dlc) = row
                except(Exception):
                    raise ValueError("shit")  # this shold be fine i think cuz all the rows have , even if no value
                    # so some  #  # should  # just be an empty string

                if name in dic:
                    print(f"Duplicate game name found: {name}")
                else:
                    dic[name] = True

    def testing_thing_hi(self):
        for game_id in self._vertices:
            g = self._vertices[game_id].item
            print(g.id)
            print(g.price)
            print(g.description)
            print(g.languages)
            print(g.image)
            print(g.requirements)
            print(g.developers)
            print(g.platforms)
            print(g.categories)
            print(g.genres)
            print(g.dlc)
            break


def load_graph(data_file: str) -> Graph:
    """ Loads a new graph with verticies given by a csv data_file

    Preconditions
    """
    graph = Graph()
    with open(data_file, 'r', encoding='utf8') as file:
        reader = csv.reader(file)
        row = next(reader)
        for row in reader:
            if len(row) != 12:
                print(i, row[0])
            game = _load_game_object(row)
            graph.add_vertex(game)
    return graph


def _load_game_object(game_data: list[str | bool]) -> Game:
    """ Helper function for load_graph which creates a Game object using a list of game_data

    """
    (id, name, price_overview, description, supported_languages, capsule_image, requirements, developers, platforms,
     categories, genres, dlc) = game_data
    name = name[1:-1]
    if price_overview == 'unknown':
        price_overview = None
    else:
        price_overview = ast.literal_eval(price_overview)
    if supported_languages == '':
        supported_languages = None
    else:
        supported_languages = ast.literal_eval(supported_languages)

    requirements = requirements[7:-1]
    lst1 = requirements.split(", 'Mac': ")
    pc = lst1[0][1:-1]
    lst2 = lst1[1].split(", 'Linux': ")
    mac = lst2[0][1:-1]
    linux = lst2[1][1:-1]
    requirements = {'PC': pc, 'Mac': mac, 'Linux': linux}

    if developers == '':
        developers = None
    else:
        developers = ast.literal_eval(developers)
    if platforms == '':
        platforms = None
    else:
        platforms = ast.literal_eval(platforms)
    if categories == '':
        categories = None
    else:
        categories = ast.literal_eval(categories)
    if genres == '':
        genres = None
    else:
        genres = ast.literal_eval(genres)
    dlc = dlc == 'True'

    return Game(id, name, price_overview, description, supported_languages, capsule_image, requirements, developers,
                platforms, categories, genres, dlc)


def extract_freq(data_file: str):
    with open(data_file, 'r', encoding='utf8') as file:
        reader = csv.reader(file)
        row = next(reader)
        row = 'useless'
        row = ':('
        dic_categories = {}
        dic_genres = {}
        for i, row in enumerate(reader):
            categories = ast.literal_eval(row[9])
            genres = ast.literal_eval(row[10])
            for x in categories:
                dic_categories[x] = dic_categories.get(x, 0) + 1
            for x in genres:
                dic_genres[x] = dic_genres.get(x, 0) + 1
            categories_items = sorted(dic_categories.items(), key=lambda x: (-x[1], x[0]))
            genres_items = sorted(dic_genres.items(), key=lambda x: (-x[1], x[0]))
        return [x[0] for x in categories_items], [x[0] for x in genres_items]


print(extract_freq('data.csv'))
g = Graph()
g.build_graph('data.csv', 10)

with open('old_files/old_data.csv', 'r', encoding='utf8') as file:
    reader = csv.reader(file)
    row = next(reader)
    row = 'useless'
    row = ':('
    dic = {}

    for x in reader:
        x = x[4]
        list = x.split(',')
        for i, a in enumerate(list):
            if '<' in a:
                list.pop(i)
                list.extend(a.split('<'))
        for x in list:
            dic[x] = dic.get(x, 0) + 1

with open('data.csv', 'r', encoding='utf8') as file:
    reader = csv.reader(file)
    row = next(reader)
    row = 'useless'
    row = ':('
    dic = {}

    for x in reader:
        x = x[4]
        list = ast.literal_eval(x)
        for i in list:
            dic[i] = dic.get(i, 0) + 1

with open('data.csv', 'r', encoding='utf8') as file:
    reader = csv.reader(file)
    row = next(reader)
    row = 'useless'
    row = ':('
    dic = {}
    for x in reader:
        x = x[6]
        x = x[7:-1]
        #print(x)
        lst1 = x.split(", 'Mac': ")
        pc = lst1[0][1:-1]
        lst2 = lst1[1].split(", 'Linux': ")
        mac = lst2[0][1:-1]
        linux = lst2[1][1:-1]
        dic = {'PC': pc, 'Mac': mac, 'Linux': linux}
        #print(dic)

print(dic)
