# Description:
# Created by Emilia on 2025-03-23
from __future__ import annotations

import ast
import csv
from random import randint, random
from typing import Any, Optional, Union

from attr import dataclass

from typing import Any

from pandas.core.computation.common import result_type_many
from pandas.core.config_init import pc_max_info_rows_doc

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
        - id: The id of the Game object
        - item: The Game object stored in this vertex.
        - neighbours: The vertices that are adjacent to this vertex.

    Representation Invariants:
        - self not in self.neighbours
        - all(self in u.neighbours for u in self.neighbours)
    """
    item_id: int
    item: Game
    neighbours: dict[_Vertex, Union[int, float]]

    def __init__(self, item: Game) -> None:
        """Initialize a new vertex with the given item and neighbours."""
        self.item_id = item.id
        self.item = item
        self.neighbours = {}

    def check_connected(self, target_item_id: int, visited: set[_Vertex]) -> bool:
        """Return whether this vertex is connected to a vertex corresponding to the target_item_id,
        WITHOUT using any of the vertices in visited.

        Preconditions:
            - self not in visited
        """
        if self.item_id == target_item_id:
            return True
        else:
            visited.add(self)
            for u in self.neighbours:
                if u not in visited:
                    if u.check_connected(target_item_id, visited):
                        return True
            return False

    def clear_neighbours(self) -> None:
        """ Remove all neighbours of this vertex and remove this vertex from the list of neighbours of each neighbour
        """
        for neighbour in self.neighbours:
            neighbour.neighbours.pop(self)
        self.neighbours = {}

    def clear_all_edges(self) -> None:
        """ Remove all neighbours of this vertex and remove this vertex from the list of neighbours of each neighbour,
        then clear all neighbours of each neighbour etc?
        """
        for neighbour in self.neighbours:
            neighbour.neighbours.pop(self)
            self.neighbours.pop(neighbour)
            neighbour.clear_neighbours()

    def calculate_score(self, other: _Vertex, preferences) -> float:
        """ Calculate the score between this vertex and another vertex based on a dictionary? of weighted preferences.

        """
        # TODO: implement this
        return 69


class Graph:
    """A graph.

    Representation Invariants:
        - all(item_id == self._vertices[item_id].item_id for item_id in self._vertices)
    """
    # Private Instance Attributes:
    #     - _vertices:
    #         A collection of the vertices contained in this graph.
    #         Maps item_id to _Vertex object.
    _vertices: dict[int, _Vertex]

    def __init__(self) -> None:
        """Initialize an empty graph (no vertices or edges)."""
        self._vertices = {}

    def add_vertex(self, item: Game) -> None:
        """Add a vertex with the given item to this graph.

        The new vertex is not adjacent to any other vertices.

        Preconditions:
            - item not in self._vertices
        """
        if item.id not in self._vertices:
            self._vertices[item.id] = _Vertex(item)

    def add_edge(self, item_id1: int, item_id2: int, weight: Union[int, float]) -> None:
        """Add an edge between the two vertices with the given item_ids in this graph,
        with the given weight.

        Raise a ValueError if item_id1 or item_id2 do not appear as vertices in this graph.

        Preconditions:
            - item_id1 != item_id2
        """
        if item_id1 in self._vertices and item_id2 in self._vertices:
            v1 = self._vertices[item_id1]
            v2 = self._vertices[item_id2]

            # Add the new edge
            v1.neighbours[v2] = weight
            v2.neighbours[v1] = weight
        else:
            # We didn't find an existing vertex for both items.
            raise ValueError

    def get_weight(self, item_id1: int, item_id2: int) -> Union[int, float]:
        """Return the weight of the edge between the given item_ids.

        Return 0 if item_id1 and item_id2 are not adjacent.

        Preconditions:
            - item_id1 and item_id2 are vertices in this graph
        """
        v1 = self._vertices[item_id1]
        v2 = self._vertices[item_id2]
        return v1.neighbours.get(v2, 0)

    def get_vertex(self, item_id: Any) -> _Vertex:
        """
        Returns the vertex given a corresponding item_id.
        """
        return self._vertices[item_id]

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
                    raise ValueError(
                        "shit")  # this shold be fine i think cuz all the rows have , even if no value  # so some  #
                    # should  # just be an empty string

                if name in dic:
                    print(f"Duplicate game name found: {name}")
                else:
                    dic[name] = True

    def testing_thing_hi(self):
        """
        just testing stuff out
        """
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

    def clear_edges(self) -> None:
        """ Clear/remove all edges in this graph
        """
        for game_id in self._vertices:
            self._vertices[game_id].clear_neighbours()

    def clear_edges_alt(self, target_id) -> None:
        """ Starting from a target vertex with the target_id, clear all the edges of every vertex connected to this
        target vertex. (this might be more efficient if we make the graph using only one starting game and keep
        track of the id of that game)
        """
        self._vertices[target_id].clear_all_edges()

    def build_edges(self, filters, preferences, target_id: int) -> None:
        """ Given a dictionary? or something of filters and preferences, add edges in the graph.
        filters are mandatory (like os and stuff), which preferences are not (maybe weighted based on importance).
        Create edges between the vertex with target_id and all other vertexes that satisfy the filters, and add weights
        to each edge calculated using preferences and maybe other factors?

        we should also build edges between other vertexes that arent the target one but idk how that would work
        """
        for vertex_id in self._vertices:
            # if satisfy_filters(target_id, vertex_id):
            if vertex_id != target_id:
                score = self.get_score(target_id, vertex_id, preferences)
                self.add_edge(target_id, vertex_id, score)

    def get_score(self, item_id1: int, item_id2: int, preferences) -> float:
        """Return the score between the two given games in this graph given their ids.

        Preferences is a collection of weighted preferences of the user used to calculate the score

        Raise a ValueError if item_id1 or item_id2 do not appear as vertices in this graph.

        Preconditions:
            -
        """
        if item_id1 not in self._vertices or item_id2 not in self._vertices:
            raise ValueError
        else:
            return self._vertices[item_id1].calculate_score(self._vertices[item_id2], preferences)

    def recommend_games(self, target_id: int, limit: int) -> list[str]:
        """ call this to return a list of game ids or names or something, closest to game with target_id, with
        limited number of recommendations
        """
        games = []
        vertex = self._vertices[target_id]
        visited = {vertex}
        for game_vertex in vertex.neighbours:
            self._add_recommendation_in_order(vertex, game_vertex, games)
        return games[0:limit]

    def _add_recommendation_in_order(self, target_vertex: _Vertex, new_vertex: _Vertex, game_list: list[int]) -> None:
        """
        Helper function for recommend_games that adds a new_game to a list of game ids (game_list) in
        descending order of similarity score with target_book, and in alphabetical order of game name in the case of
        equal similarity scores.
        """
        for i in range(len(game_list)):
            game_id = game_list[i]
            sim_score = self.get_weight(target_vertex.item_id, game_id)
            new_sim_score = self.get_weight(target_vertex.item_id, new_vertex.item_id)
            if sim_score < new_sim_score or (sim_score == new_sim_score and self._vertices[game_id].item.name <
                                             new_vertex.item.name):
                game_list.insert(i, new_vertex.item_id)
                return
        game_list.append(new_vertex.item_id)
        return


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
    """ Helper for _load_game_object, use and return ast.literal_eval() on a given string, unless the string is equal to
    the exclude string, then return None
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
    id = int(id)
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


def build_dic(data_file: str) -> dict:
    # Here we are using the 'encoding=' to make sure everyone's computer will be able to use the csv file
    with open(data_file, 'r', encoding='utf8') as file:
        reader = csv.reader(file)
        row = next(reader)
        row = 'useless'
        row = ':('

        dic = {}
        for i, row in enumerate(reader):
            # print(row)
            if len(row) != 12:
                print(i, row[0])
                print("NOOOO")
            try:
                (id, name, price_overview, description, supported_languages, capsule_image, requirements, developers,
                 platforms, categories, genres, dlc) = row
                d1 = {}
                d1['name'] = name
                d1['price_overview'] = price_overview
                d1['description'] = description
                d1['supported_languages'] = supported_languages
                d1['capsule_image'] = capsule_image
                d1['requirements'] = requirements
                d1['developers'] = developers
                d1['platforms'] = platforms
                d1['categories'] = categories
                d1['genres'] = genres
                d1['dlc'] = dlc
                dic[id] = d1
            except(Exception):
                raise ValueError(
                    "shit")  # this shold be fine i think cuz all the rows have , even if no value  # so some  #  #
                # should  # just be an empty string
        return dic


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

        l = [[row[0], row[1], row[2], row[3], row[5], ast.literal_eval(row[10])] for row in reader]
        for i,row in enumerate(l):
            try:
                dictified = ast.literal_eval(row[2])['final']
                l[i][2] = dictified
            except:
                l[i][2] = 'unknown'
    while len(gamers) < 25:
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
# print(dic)

if __name__ == "__main__":
    graph = load_graph('data.csv')
    graph.build_edges(1, 1, 1291240)
    graph.testing_thing_hi()
    print(graph.get_score(1291240, 1291170, 1))
    print(graph.get_weight(1291240, 1291170))
