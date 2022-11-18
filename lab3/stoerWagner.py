from dimacs import loadWeightedGraph
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
        
def mergeVertices(graph, x, y): # do wierzchołka x dołączany jest wierzchołek y
    for to in graph[y].edges:
        graph[to].delEdge(y)
        if to == x: continue
        graph[x].addEdge(to, graph[y].edges[to])
        graph[to].addEdge(x, graph[y].edges[to])  
    graph[x].mergedWith.append(y)
    graph[x].mergedWith += graph[y].mergedWith
    graph[y].activated = False
    
def minCutPhase(graph):
    a = 0
    S = {graph[0]}
    q = PriorityQueue()
    weightSum = [0 for _ in range(len(graph))]
    for i in range(1, len(graph)):
        weightSum[i] += graph[i].get(a, 0)
    for i in range(1, len(graph)):
        q.put((-weightSum[i], i))
    visited = [False for _ in range(len(graph))]
    
    s, t = 0, 0
    while len(S) < len(graph):
        val, v = q.get()
        if visited[v]:
            continue        
        val = -val
        for to in graph[v].edges:
            weightSum[to] += graph[to].get(v, 0)
            q.put()

        
        
        
        

def stoerWagner(dimacsFile):
    (V, L) = loadWeightedGraph(dimacsFile)
    graph = [Node() for _ in range(V)]
    for (x, y, c) in L:
        graph[x-1].addEdge(y-1, c)
        graph[y-1].addEdge(x-1, c)
    printGraph(graph)
    print(V)
    print("mergetest")
    mergeVertices(graph, 0, 1)
    printGraph(graph)
    mergeVertices(graph, 3, 4)
    print("second merge")
    printGraph(graph)
    print("third merge")
    mergeVertices(graph, 0, 3)
    printGraph(graph)
stoerWagner("graphs/clique5")
    