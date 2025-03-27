# Description:
# Created by Emilia on 2025-03-23
from __future__ import annotations

import ast
import csv
from random import randint
from typing import Any, Optional, Union

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
                    id, name, price_overview, description, supported_languages, capsule_image, requirements, developers,
                    platforms, categories, genres, dlc) = row
                except(Exception):
                    raise ValueError(
                        "shit")  # this shold be fine i think cuz all the rows have , even if no value  # so some  #
                    # should  # just be an empty string

                if name in dic:
                    print(f"Duplicate game name found: {name}")
                else:
                    dic[name] = True

    def testing_thing_hi(self):
        for game_id in self._vertices:
            g = self._vertices[game_id].item
            print(g.id)
            print(g.name)
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
                print(row[0])
            game = _load_game_object(row)
            graph.add_vertex(game)
    return graph


def _get_object_from_string(string: str, exclude: Optional[str] = "") -> Any:
    """ Helper for _load_game_object

    """
    if string == exclude:
        return None
    else:
        try:
            return ast.literal_eval(string)
        except:
            print(string)
            print('L')



def _load_game_object(game_data: list[str | bool]) -> Game:
    """ Helper function for load_graph which creates a Game object using a list of game_data

    """
    (id, name, price_overview, description, supported_languages, capsule_image, requirements, developers, platforms,
     categories, genres, dlc) = game_data
    name = name[1:-1]
    price_overview = _get_object_from_string(price_overview, 'unknown')
    supported_languages = _get_object_from_string(supported_languages)
    developers = _get_object_from_string(developers, 'unknown')
    platforms = _get_object_from_string(platforms)
    categories = _get_object_from_string(categories)
    genres = _get_object_from_string(genres)

    requirements = requirements[7:-1]
    lst1 = requirements.split(", 'Mac': ")
    pc = lst1[0][1:-1]
    lst2 = lst1[1].split(", 'Linux': ")
    mac = lst2[0][1:-1]
    linux = lst2[1][1:-1]
    requirements = {'PC': pc, 'Mac': mac, 'Linux': linux}

    dlc = dlc == 'True'

    return Game(id, name, price_overview, description, supported_languages, capsule_image, requirements, developers,
                platforms, categories, genres, dlc)


g = Graph()
g.build_graph('data.csv', 10)


def extract_freq(data_file: str, col: int):
    with open(data_file, 'r', encoding='utf8') as file:
        reader = csv.reader(file)
        row = next(reader)
        row = 'useless'
        row = ':('
        dic = {}
        for i, row in enumerate(reader):
            colle = ast.literal_eval(row[col])
            for x in colle:
                dic[x] = dic.get(x, 0) + 1

            col_items = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
        return [x[0] for x in col_items]


# random button in main menu to select random games to look through
def random_selection():
    gamers = []
    with open('data.csv', 'r', encoding='utf8') as file:
        reader = csv.reader(file)
        row = next(reader)
        row = 'useless'
        row = ':('
        l = [row[0] for row in reader]
    while len(gamers) < 20:
        num = randint(2, 2069)
        gamers.append(l[num-2])
    return gamers
"""
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
"""
#print(dic)

if __name__ == "__main__":
    g = load_graph('data.csv')
    g.testing_thing_hi()
