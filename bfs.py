# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 22:31:13 2020
@author: trohit
"""
from collections import deque
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
def bfs(graph:dict, v:set, n:str):
    if n not in v:
        print(n)
        print("(+) v add " + n)
        v.add(n)
    # add neighs to q
    if not n in graph.keys():
        print("(^) unwind")
        return
    for c in graph[n]:
        print("=> q add " + c)
        q.appendleft(c)
    while len(q):
        n2 = q.pop()
        print("(-) pop :" + n2)
        bfs(graph, v, n2)
# main         
bfs(graph, visited, 'a')

     
