import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from edmondBFS import edmondsKarp
from copy import deepcopy
from dimacs import loadWeightedGraph
from runtest import runtest

def changeToMatrix(V, E):
    R = [[0 for _ in range(V)] for _ in range(V)]
    for el in E:
        R[el[0]-1][el[1]-1] = el[2]
        R[el[1]-1][el[0]-1] = el[2]
    return R


def makeAdjList(V, L):
    R = [[] for _ in range(V)]
    for el in L:
        R[el[0]-1].append(el[1]-1)
        R[el[1]-1].append(el[0]-1)
    return R


def sol(A):
    (V, E) = loadWeightedGraph(A)
    graphMatrix = changeToMatrix(V, E)
    graphAdjList = makeAdjList(V, E)
    s = 0
    minMaxFlow = float("inf")
    for t in range(1, V):
        if V > 150:
            return edmondsKarp(graphMatrix, graphAdjList, s, V-1)
        mat = deepcopy(graphMatrix)
        adj = deepcopy(graphAdjList)
        minMaxFlow = min(minMaxFlow, edmondsKarp(mat, adj, s, t))
    return minMaxFlow

graphs = os.path.dirname(os.path.abspath(__file__)) + "\\graphs\\connectivity"

runtest(sol, graphs)
