# -*- coding: utf-8 -*-
"""SSSP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15QnRmeqWbuZdGh5YYXOAX6lQujRkWpAj
"""

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def bfs(self, start, end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)

customDict = { "a" : ["b", "c"],
               "b" : ["d", "g"],
               "c" : ["d", "e"],
               "d" : ["f"],
               "e" : ["f"],
               "g" : ["f"]
            }

g = Graph(customDict)
print(g.bfs("a", "z"))