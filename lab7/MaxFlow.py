import networkx as nx
from networkx.algorithms.flow import *
from genericpath import isfile
from os import listdir
from dimacs import loadDirectedWeightedGraph, readSolution


def flow(file):
    
    (V, L) = loadDirectedWeightedGraph(file)

    G = nx.DiGraph()
    
    for i in range(1, V + 1):
        G.add_node(i)
    
    for (u, v, t) in L:
        G.add_edge(u, v)
        G[u][v]['capacity'] = t

    return maximum_flow(G, 1, V)[0]


def test():
    areThereProblems = False
    graphs = listdir("graphs//flow")
    print (graphs)

    for graph in graphs:
        if not isfile("graphs/flow/" + graph):
            continue
        f = open("graphs/flow/" + graph, "r")
        ans = int(readSolution("graphs/flow/" + graph))
        print("============================")
        print("filename: " + graph)
        myans = flow("graphs/flow/" + graph)
        if ans != myans:
            areThereProblems = True
        
        print("given solution: ", ans)
        print("my solution: ", myans)
        print("answer is " + "correct" if myans == ans else "uncorrect")
    return areThereProblems

if not test():
    print("All tests passed!")
else:
    print("There are problems.")
