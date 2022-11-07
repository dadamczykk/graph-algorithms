from edmondBFS import edmondsKarp
from dimacs import readSolution
from os import listdir
from os.path import isfile
from dimacs import loadWeightedGraph, loadDirectedWeightedGraph
from copy import deepcopy

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

def test():
    graphs = listdir("graphs/connectivity/")
    print (graphs)
    areThereProblems = False

    for graph in graphs:
        if not isfile("graphs/connectivity/" + graph):
            continue
        f = open("graphs/connectivity/" + graph, "r")
        ans = int(readSolution("graphs/connectivity/" + graph))
        print("============================")
        print("filename: " + graph)
        myans = sol("graphs/connectivity/" + graph)
        if ans != myans:
            areThereProblems = True
        
        print("given solution: ", ans)
        print("my solution: ", myans)
        print("answer is " + "correct" if myans == ans else "uncorrect")

    if areThereProblems:
        print("\n\n=== There are some mistakes")
    else:
        print("\n\n=== All correct!")
test()