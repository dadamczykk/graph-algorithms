from edmondBFS import edmondsKarp
from dimacs import readSolution
from os import listdir
from os.path import isfile
from dimacs import loadDirectedWeightedGraph

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

def test():
    graphs = listdir("graphs/flow/")
    print (graphs)
    areThereProblems = False

    for graph in graphs:
        
        if not isfile("graphs/flow/" + graph):
            continue
        f = open("graphs/flow/" + graph, "r")
        line = f.readline()
        ans = int(readSolution("graphs/flow/" + graph))
        myans = sol("graphs/flow/" + graph)
        if ans != myans:
            areThereProblems = True
        print("============================")
        print("filename: " + graph)
        print("given solution: ", ans)
        print("my solution: ", myans)
        print("answer is " + "correct" if myans == ans else "uncorrect")
    if areThereProblems:
        print("\n\n=== There are some mistakes")
    else:
        print("\n\n=== All correct!")
test()