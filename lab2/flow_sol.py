import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from edmondBFS import edmondsKarp
from dimacs import loadDirectedWeightedGraph
from runtest import runtest

def changeToMatrix(V, E):
    R = [[0 for _ in range(V)] for _ in range(V)]
    for el in E:
        R[el[0]-1][el[1]-1] = el[2]
    return R

def makeAdjList(V, L):
    R = [[] for _ in range(V)]
    for el in L:
        R[el[0]-1].append(el[1]-1)
        R[el[1]-1].append(el[0]-1)
    return R
    

def sol(A):
    (V, E) = loadDirectedWeightedGraph(A)
    graphMatrix = changeToMatrix(V, E)
    graphAdjList = makeAdjList(V, E)
    s, t = 0, V - 1
    return edmondsKarp(graphMatrix, graphAdjList, s, t)

graphs = os.path.dirname(os.path.abspath(__file__)) + "\\graphs\\flow"

runtest(sol, graphs)