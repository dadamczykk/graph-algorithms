import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dimacs import loadWeightedGraph

class Node:
    def __init__(self, idx):
        self.idx = idx
        self.out = set()

    def connect_to(self, v):
        self.out.add(v)
        
def lex_BFS(G):
    n = len(G)
    visited = []
    sets = [set([i for i in range(1,n)]), {0}]
    right_neighbours = [None for _ in range(n)]
    parent = [None for _ in range(n)]
    
    while len(sets) > 0:
        v = sets[-1].pop()
        visited.append(v)
        
        if len(sets[-1]) == 0:
            sets.pop()
        
        iterator = 0
        
        while iterator < len(sets):
            Y = G[v].out & sets[iterator]
            K = sets[iterator] - Y
            insert_point = iterator
            if len(Y) > 0:
                sets.insert(insert_point + 1, Y)
                iterator += 1
            if len(K) > 0:
                sets.insert(insert_point + 1, K)
                iterator += 1
            sets.pop(insert_point)
        
        right_neighbours[v] = set(visited) & G[v].out
        
        for vertex in visited[::-1]:
            if vertex in right_neighbours[v]:
                parent[v] = vertex
                break
    
    return visited, right_neighbours, parent
        

def read_graph(graph):
    V, L = loadWeightedGraph(graph)
    G = [Node(i) for i in range(V)]
    for (u, v, _) in L:
        G[u - 1].connect_to(v - 1)
        G[v - 1].connect_to(u - 1)
    return G
