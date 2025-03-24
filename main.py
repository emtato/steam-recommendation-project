# Description:
# Created by Emilia on 2025-03-23
from __future__ import annotations

import csv
import tkinter as tk
from typing import Any

# weight of each category for determining matches
# we can create a simple ranking system where the user ranks whats most important to them for personalization
genre, languages, platforms = 0, 0, 0


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
    neighbours: set[_Vertex]

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
            - item not in self._vertices
        """
        if item not in self._vertices:
            self._vertices[item] = _Vertex(item, set())

    def add_edge(self, item1: Any, item2: Any) -> None:
        """Add an edge between the two vertices with the given items in this graph.

        Raise a ValueError if item1 or item2 do not appear as vertices in this graph.

        Preconditions:
            - item1 != item2
        """
        if item1 in self._vertices and item2 in self._vertices:
            v1 = self._vertices[item1]
            v2 = self._vertices[item2]

            v1.neighbours.add(v2)
            v2.neighbours.add(v1)
        else:
            raise ValueError

    def build_graph(self, data_file: str, amount: int) -> Graph:
        with open(data_file, 'r') as file:
            reader = csv.reader(file)
            row = next(reader)
            row = 'you are useless garbo header row no one needs you'
            row = ':('
            for i,row in enumerate(reader):
                print(row)
                if i >= amount-1:
                    break


g = Graph()
g.build_graph('data.csv', 10)


def option_selected(value):
    print(f"Selected: {value}")


root = tk.Tk()
root.title("Dropdown Example")

options = ["Option 1", "Option 2", "Option 3"]
selected = tk.StringVar(value=options[0])

dropdown = tk.OptionMenu(root, selected, *options, command=option_selected)
dropdown.pack(pady=20)

root.mainloop()
