import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dimacs import loadWeightedGraph
from runtest import runtest
from queue import PriorityQueue

class Node:
    def __init__(self):
        self.edges = {}
        self.activated = True
        self.mergedWith = []

    def addEdge(self, to, weight):
        self.edges[to] = self.edges.get(to, 0) + weight
    
    def delEdge(self, to):
        del self.edges[to]
    
    def __str__(self):
        return str(self.edges)

def printGraph(graph):
    for el in graph:
        print(el, el.mergedWith, el.activated)
        
def merge_vertices(graph, x, y): # y vertex is connected to x vertex
    for to in graph[y].edges:
        if graph[to].edges.get(y, 0) != 0:
            graph[to].delEdge(y)
        if to == x: continue
        graph[x].addEdge(to, graph[y].edges[to])
        graph[to].addEdge(x, graph[y].edges[to])  
    # graph[x].mergedWith.append(y)
    # graph[x].mergedWith += graph[y].mergedWith
    graph[y].activated = False
    
    
def min_cut_phase(graph, activeVertex):
    a = 0
    S = {a}
    q = PriorityQueue()
    s, t = 0, 0
    potentialAns = float("inf")    
    weightSum = [0 for _ in range(len(graph))]
    visited = [False for _ in range(len(graph))]    

    q.put((-float("inf"), a))
    
    while len(S) < activeVertex:
        val, v = q.get()
        if visited[v]:
            continue
        
        for to in graph[v].edges:
            if visited[to] or to in S: continue
            weightSum[to] += graph[to].edges.get(v, 0)
            q.put((-weightSum[to], to))

        visited[v] = True
        S.add(v)
        potentialAns = -val
        t = s
        s = v
    merge_vertices(graph, s, t)
    
    return potentialAns


def stoer_wagner(dimacsFile):
    (V, L) = loadWeightedGraph(dimacsFile)
    graph = [Node() for _ in range(V)]
    
    for (x, y, c) in L:
        graph[x-1].addEdge(y-1, c)
        graph[y-1].addEdge(x-1, c)
    # mergeVertices(graph, 0, 1)
    # printGraph(graph)
    ans = float("inf")
    for i in range(V):
        # if i%100 == 0:
        #     print(i, end=" ")
        ans = min(ans, min_cut_phase(graph, V - i))
    return ans
        
graphs = os.path.dirname(os.path.abspath(__file__)) + "\\graphs"

runtest(stoer_wagner, graphs)