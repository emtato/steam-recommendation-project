# Description: This python file contains the code for the Game class, the graph/vertex classes (with their creation
# functions). This also contains the functions for game filtering, and the graph similarity/weighing code for finding
# similar games to the chosen one.
# Created by Emilia, Amanda, Nicole, Grace on 2025-03-23
from __future__ import annotations

import ast
import csv
from random import randint
from typing import Optional, Union
from attr import dataclass
from typing import Any

PRICE, LANGUAGE, DEV, PLATFORM, CATEGORY, GENRE = 0, 1, 2, 3, 4, 5


@dataclass
class Game:
    """
    Game dataclass object containing information about a steam game.
    Instance Attributes:
        - id: The unique id of this game
        - name: The name of this game
        - price: A dictionary representing information about the price, or None if price is unknown
        - description: A description of this game
        - languages: A list of the languages this game supports
        - image: A link to an image of this game
        - requirements: A dictionary mapping operating systems to their requirements
        - developers: A list of names of this game's developers, or None if unknown
        - platforms: A dictionary mapping operating systems to a boolean representing whether this system is supported
        - categories: A list of categories this game falls under
        - genres: A list of genres this game falls under
        - dlc: A boolean value representing whether this game is a dlc

    Representation Invariants:
        -
    """
    id: int
    name: str
    price: Optional[dict[str:Any]]
    description: str
    languages: list[str]
    image: str
    requirements: dict[str: str]
    developers: Optional[list[str]]
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
        """Initialize a new vertex with the given game item and neighbours."""
        self.item_id = item.id
        self.item = item
        self.neighbours = {}

    def clear_neighbours(self) -> None:
        """ Remove all neighbours of this vertex and remove this vertex from the list of neighbours of each neighbour
        """
        for neighbour in self.neighbours:
            neighbour.neighbours.pop(self)
        self.neighbours = {}

    def _calculate_sim(self, this_list: Optional[list[str]], other_list: Optional[list[str]]) -> float:
        """Helper function for calculate score that calculates the similarity between
        two lists. Returns 0 if either list is None"""
        if this_list is None or other_list is None or len(this_list) == 0 or len(other_list) == 0:
            return 0.0
        else:
            return (len(set(this_list).intersection(set(other_list))) /
                    len(set(this_list).union(set(other_list))))

    def calculate_score(self, other: _Vertex, preferences: list[int]) -> float:
        """ Calculate the score between this vertex and another vertex based on a list of preference weights.
        Preconditions:
            - self.item_id != other.item_id
            - len(preferences) == 6
            - all({num >= 0 and num <= 100 for num in preferences})
        """
        this_game = self.item
        other_game = other.item

        if this_game.price is None or other_game.price is None:
            price_sim = 0
        elif this_game.price['final'] == 0 and other_game.price['final'] == 0:
            price_sim = 1
        else:
            price_sim = 1 - abs(this_game.price['final'] - other_game.price['final']) / (
                    2 * (this_game.price['final'] + other_game.price['final']))

        lang_sim = self._calculate_sim(this_game.languages, other_game.languages)
        dev_sim = self._calculate_sim(this_game.developers, other_game.developers)
        cat_sim = self._calculate_sim(this_game.categories, other_game.categories)
        gen_sim = self._calculate_sim(this_game.genres, other_game.genres)

        both_true_platforms = 0
        one_true_platforms = 0
        for plat in this_game.platforms:
            both_true_platforms += int(this_game.platforms[plat] and other_game.platforms[plat])
            one_true_platforms += int(this_game.platforms[plat] or other_game.platforms[plat])
        if one_true_platforms == 0:
            plat_sim = 0.0
        else:
            plat_sim = both_true_platforms / one_true_platforms

        return (price_sim * preferences[PRICE] + lang_sim * preferences[LANGUAGE] + dev_sim * preferences[DEV] +
                plat_sim * preferences[PLATFORM] + cat_sim * preferences[CATEGORY] + gen_sim * preferences[GENRE]) / (
            600)


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
        """Add a vertex with the given game item to this graph.
        The new vertex is not adjacent to any other vertices.
        Add the game id of the item as the key and the _Vertex object as the value.
        """
        if item.id not in self._vertices:
            self._vertices[item.id] = _Vertex(item)

    def add_edge(self, item_id1: int, item_id2: int, weight: Union[int, float]) -> None:
        """Add an edge between the two vertices with the given item_ids in this graph, with the given weight.
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

    def _get_weight(self, item_id1: int, item_id2: int) -> Union[int, float]:
        """Return the weight of the edge between the vertices with the given item_ids.
        Return 0 if item_id1 and item_id2 are not adjacent.

        Preconditions:
            - item_id1 in self._vertices
            - item_id2 in self._vertices
        """
        v1 = self._vertices[item_id1]
        v2 = self._vertices[item_id2]
        return v1.neighbours.get(v2, 0)

    def get_avg_weight(self, item_ids: list[int], target_id: int) -> Union[int, float]:
        """ Return the average weight between the edges of a list of vertices with the given
        item_ids, and the vertex with the target_id.

        Preconditions:
            - all({item_id in self._vertices for item_id in item_ids})
            - target_id in self._vertices
            - len(item_ids) >= 1
        """
        total_weights = 0.0
        for item_id in item_ids:
            total_weights += self._get_weight(item_id, target_id)
        return total_weights / len(item_ids)

    def get_vertex(self, item_id: Any) -> _Vertex:
        """
        Returns the vertex given a corresponding item_id.

        Preconditions:
            - item_id in self._vertices
        """
        return self._vertices[item_id]

    def clear_edges(self) -> None:
        """ Clear/remove all edges in this graph
        """
        for game_id in self._vertices:
            self._vertices[game_id].clear_neighbours()

    def build_edges(self, preferences: list[int]) -> None:
        """ Given a list of preference weights, add edges in the graph.

        Preconditions:
            - len(preferences) == 6
            - all({num >= 0 and num <= 100 for num in preferences})
        """
        vertex_list = list(self._vertices.keys())
        for i in range(len(vertex_list)):
            for j in range(i + 1, len(vertex_list)):
                vertex_id1 = vertex_list[i]
                vertex_id2 = vertex_list[j]
                score = self.get_score(vertex_id1, vertex_id2, preferences)
                self.add_edge(vertex_id1, vertex_id2, score)

    def get_score(self, item_id1: int, item_id2: int, preferences: list[int]) -> float:
        """Return the score between the two given games in this graph given their ids and a list of weights
        representing the user's preferences.

        Raise a ValueError if item_id1 or item_id2 do not appear as vertices in this graph.

        Preconditions:
            - len(preferences) == 6
            - all({num >= 0 and num <= 100 for num in preferences})
        """
        if item_id1 not in self._vertices or item_id2 not in self._vertices:
            raise ValueError
        else:
            return self._vertices[item_id1].calculate_score(self._vertices[item_id2], preferences)

    def recommend_games(self, target_ids: list[int], limit: int) -> list[Game]:
        """ Recommend a list with length limit of Game objects with scores closest to the games with the target_id(s).

        Preconditions:
            - limit >= 0
            - all({target_id in self._vertices for target_id in target_ids})
            - len(target_ids) >= 1
        """
        games = []
        for game_id in self._vertices:
            if game_id not in target_ids:
                self._add_recommendation_in_order(target_ids, game_id, games)
        game_ids = games[0:limit]
        return [self._vertices[game_id].item for game_id in game_ids]

    def _add_recommendation_in_order(self, target_ids: list[int], new_id: int, game_list: list[int]) -> None:
        """
        Helper function for recommend_games that adds a new_id to a list of game ids (game_list) in
        descending order of score with the list of target_ids.
        """
        for i in range(len(game_list)):
            curr_id = game_list[i]
            curr_sim_score = self.get_avg_weight(target_ids, curr_id)
            new_sim_score = self.get_avg_weight(target_ids, new_id)
            if curr_sim_score < new_sim_score:
                game_list.insert(i, new_id)
                return
            elif (curr_sim_score == new_sim_score and self._vertices[curr_id].item.name <
                  self._vertices[new_id].item.name):
                random_num = randint(1, 2)
                if random_num == 1:
                    game_list.insert(i, new_id)
                    return
            return
        game_list.append(new_id)
        return


def list_games(data_file: str) -> list:
    """
    returns a list of all game objects (based on the given data file)
    """
    lst = []
    with open(data_file, 'r', encoding='utf8') as file:
        reader = csv.reader(file)
        row = next(reader)
        for row in reader:
            game = _load_game_object(row)
            lst.append(game)
    return lst


def load_graph(data_file: str) -> Graph:
    """ Loads a new graph with verticies given by a csv data_file

    Preconditions:
        - data_file is the path to a CSV file corresponding to data about steam games used for this project.
    """
    graph = Graph()
    with open(data_file, 'r', encoding='utf8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if len(row) != 12:
                print(row[0])
            game = _load_game_object(row)
            graph.add_vertex(game)
    return graph


def _get_object_from_string(string: str, exclude: Optional[str] = None) -> Any:
    """ Helper for _load_game_object. Return a given stirng formatted as a list or dictionary as that data type,
    unless the string is equal to the exclude string, then return None.

    Preconditions:
        - if string != exclude, then string is correctly formatted as a list or dictionary
    """
    if exclude is not None and string == exclude:
        return None
    else:
        return ast.literal_eval(string)


def _load_game_object(game_data: list[str]) -> Game:
    """ Helper function for load_graph which creates a Game object using a list of game_data.
    """
    (
        game_id, name, price_overview, description, supported_languages, capsule_image, requirements, developers,
        platforms, categories, genres, dlc) = game_data
    game_id = int(game_id)
    if (name[0] == "'" and name[-1] == "'") or (name[0] == '"' and name[-1] == '"'):
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

    return Game(game_id, name, price_overview, description, supported_languages, capsule_image, requirements,
                developers,
                platforms, categories, genres, dlc)


def build_dic(data_file: str) -> dict:
    """
    This function build a dictionary with the given data_file.
    """
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
    '''this function extracts the frequency'''
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
    '''this function randomly selects games'''
    gamers = []
    with open('data.csv', 'r', encoding='utf8') as file:
        reader = csv.reader(file)
        row = next(reader)
        row = 'useless'
        row = ':('

        l = [[row[0], row[1], row[2], row[3], row[5], ast.literal_eval(row[10])] for row in reader]
        for i, row in enumerate(l):
            try:
                dictified = ast.literal_eval(row[2])['final']
                l[i][2] = dictified
            except:
                l[i][2] = 'unknown'
    while len(gamers) < 25:
        num = randint(2, 2069)
        gamers.append(l[num - 2])
    return gamers


def filtering_games(data_file: str, requirements: {}) -> list:
    """
    This function returns a list of games (in game objects) that are most similar to requirements.
    """
    games = list_games(data_file)
    similiar = []

    for g in games:
        # gets a list of all AVAILABLE platforms for the game
        TRUTH = []
        req = requirements.keys()
        total_sim, max_sim = 0, len(req)

        for comp in g.platforms.keys():
            if g.platforms[comp]:
                TRUTH.append(comp)

        # compares languages
        has_lang = True
        if "LANGUAGES" in requirements.keys():
            for lang in requirements["LANGUAGES"]:
                if lang not in g.languages:
                    has_lang = False
            if has_lang:
                total_sim += 1

            # compares os + os specfifics
            if "COMPUTER" in requirements.keys():
                if requirements["COMPUTER"].lower() in TRUTH:
                    total_sim += 1
                    os_list, ram_list, storage_list = minimum_requirements(g, requirements["COMPUTER"])
                    print(ram_list)
                    # checks if the wanted os is in the list of possible os for game g.
                    if requirements["OS"] in os_list:
                        total_sim += 1
                    # checks if the ram requirements are over (inclusive) the minimum for game g.
                    if float(requirements["RAM"][0]) >= ram_list[0]:
                        total_sim += 1
                    # checks if the users available storage is above the minimum requirements for game g.
                    if ((float(requirements["STORAGE"][0]) >= storage_list[0]) and
                            (requirements["STORAGE"][1] == storage_list[1])):
                        total_sim += 1

        # compares genres
        has_gen = True
        if "GENRES" in requirements.keys():
            for gen in requirements["GENRES"]:
                if gen not in g.genres:
                    has_gen = False
            if has_gen:
                total_sim += 1

        # compares categories
        has_cat = True
        if "CATEGORIES" in requirements.keys():
            for cat in requirements["CATEGORIES"]:
                if cat not in g.categories:
                    has_cat = False
            if has_cat:
                total_sim += 1

        # compares prices
        if "PRICE" in requirements.keys():
            if g.price is not None:
                if float(g.price['final']) <= float(requirements["PRICE"]):
                    total_sim += 1

        if total_sim >= max_sim:
            similiar.append(g)

    return similiar


def minimum_requirements(g: Game, key: str) -> tuple:
    """
    Returns 3 lists composing of the games' minimum requirements
    - List 1: OS
    - List 2: RAM (memory), RAM (type, MB or GB)
    - List 3: Storage (float), Storage (type, MB or GB)

    Preconditions:
            - key in g.keys()
            - isinstance(g.requirements, str)
    """
    os_list, ram_list, storage_list = [], [], []

    if key == "Windows":
        key = "PC"

    # extracts the amount of storage AND the type (MB or GB)
    g_storage = g.requirements[key].split('Storage:')
    if (g_storage[0] != '') and len(g_storage) == 2:
        a = g_storage[1].split('available space')[0].split(' ')
        if not a[1].isdigit():
            storage_list.append(-1)
        else:
            storage_list.append(float(a[1]))
        storage_list.append(a[2])

    # extracts the amount of ram AND the type (MB or GB)
    g_ram = g.requirements[key].split("Memory:")
    if len(g_ram) == 2:
        ram = g_ram[1].split("RAM")[0].split(' ')
        if ram[1].isdigit():
            ram_list.append(float(ram[1]))
        else:
            ram_list.append(-1)

        ram_list.append(ram[2])

        # converts MB to GB
        if ram_list[1] == "MB":
            ram_list[0] = ram_list[0] / 1000
            ram_list[1] = "GB"

    # extracts the possible os types
    # CASE FOR PC/WINDOWS:
    if key == "PC":
        g1 = g.requirements[key].split("Processor")
        if len(g1) == 2:
            g2 = g1[0].split("Windows")
            if len(g2) == 2:
                g3 = g2[1]
                if "11" in g3:
                    os_list.append("Windows 11")
                elif "10" in g3:
                    os_list.extend(["Windows 11", "Windows 10"])
                elif "7" in g3:
                    os_list.extend(["Windows 10", "Windows 11", "Windows 7", "Windows 8"])
                elif "8" in g3:
                    os_list.extend(["Windows 8", "Windows 10", "Windows 11"])
                elif ("Vista" or "vista") in g3:
                    os_list.extend(["Windows Vista", "Windows 7", "Windows 8", "Windows 10", "Windows 11"])
                elif ("XP" or "xp") in g3:
                    os_list.extend(["Windows XP", "Windows Vista", "Windows 7", "Windows 8", "Windows 10",
                                    "Windows 11"])

    # CASE FOR MACOS VERSIONS:
    elif key == "Mac":
        g1 = g.requirements[key].split("Minimum:")
        if ([''] != g1) and (['', ''] != g1):
            g2 = g1[1].split("Processor:")[0]
            if "OS:" in g2:
                # Any MacOs, add them all
                if ("Any" in g2) and (not "Graphics:" in g2):
                    os_list.extend(["11 and below", "12", "13", "14", "15"])
                # Macos 12
                elif ("12" or "Monterey" or "monterey") in g2:
                    os_list.extend(["12", "13", "14", "15"])
                # Macos 13:
                elif ("13" or "Ventura" or "ventura") in g2:
                    os_list.extend(["13", "14", "15"])
                # macos 14
                elif ("14" or "Sonoma" or "sonoma") in g2:
                    os_list.extend(["14", "15"])
                # Macos 15
                elif ("15" or "Sequoia" or "sequoia") in g2:
                    os_list.append("15")
                # Otherwise anything 11 and below
                else:
                    os_list.extend(["11 and below", "12", "13", "14", "15"])

    # CASE FOR LINUX VERSIONS:
    elif key == "Linux":
        g1 = g.requirements[key].split("Minimum:")
        if ([''] != g1) and (['', ''] != g1) and (len(g1) == 2):
            g2 = g1[1].split("OS:")
            if len(g2) == 2:
                g3 = g2[1].split("Processor:")[0]
                if "Any" in g3:
                    os_list.extend(["Ubuntu 12", "Ubuntu 14", "Ubuntu 16", "Ubuntu 18", "Ubuntu 20", "Ubuntu 22",
                                    "SteamOS"])
                elif "Ubuntu" in g3:
                    if "12" in g3:
                        os_list.extend(
                            ["Ubuntu 12", "Ubuntu 14", "Ubuntu 16", "Ubuntu 18", "Ubuntu 20", "Ubuntu 22"])
                    elif "14" in g3:
                        os_list.extend(
                            ["Ubuntu 14", "Ubuntu 16", "Ubuntu 18", "Ubuntu 20", "Ubuntu 22"])
                    elif "16" in g3:
                        os_list.extend(
                            ["Ubuntu 16", "Ubuntu 18", "Ubuntu 20", "Ubuntu 22"])
                    elif "18" in g3:
                        os_list.extend(
                            ["Ubuntu 18", "Ubuntu 20", "Ubuntu 22"])
                    elif "20" in g3:
                        os_list.extend(
                            ["Ubuntu 20", "Ubuntu 22"])
                    elif "22" in g3:
                        os_list.append("Ubuntu 22")
                elif "SteamOS" in g3:
                    os_list.append("SteamOS")
                # Otherwise add nothing

    if not os_list:
        os_list = ['empty']
    if not ram_list:
        ram_list = [-1, 'empty']
    if not storage_list:
        storage_list = [-1, 'empty']

    return (os_list, ram_list, storage_list)


if __name__ == "__main__":
    test_graph = load_graph('data.csv')
    test_graph.build_edges([100, 0, 0, 0, 0, 0])
    # graph.testing_thing_hi()
    # print(graph.get_score(3076100, 1291170, [100, 100, 100, 100, 100, 100]))
    # print(graph.get_weight(7, 1291170))
    print([game.name for game in test_graph.recommend_games([3076100, 1291170], 20)])
    # print(test_graph._vertices[1290210].item.dlc)
    # print(graph._vertices[1291170].item.name)

    import doctest
    doctest.testmod()

    import python_ta
    python_ta.check_all(config={
        'extra-imports': [],  # the names (strs) of imported modules
        'allowed-io': [],  # the names (strs) of functions that call print/open/input
        'max-line-length': 120
    })
