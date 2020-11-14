# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 22:31:13 2020
@author: trohit
"""

"""
    A
  +-^-+
  B   C
  | +-+-+
  D E F G  
bfs:
    abcdefg

dfs:
    abdcefg
"""
visited = set()
graph = {
    'a' : list("bc"),
    'b' : list("d"),
    'c' : list("efg")
    }

def dfs(graph:dict, visited:set, node):
    if node not in visited:
        print(node, end = ",")
        visited.add(node)
    else:
        return
    if node in graph.keys():
        for neigh in graph[node]:
            dfs(graph, visited, neigh)

# main            
dfs(graph, visited, 'a')
