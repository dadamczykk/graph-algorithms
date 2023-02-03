import networkx as nx
from genericpath import isfile
from os import listdir
from networkx.algorithms.planarity import check_planarity
from dimacs import loadWeightedGraph, readSolution


def planarity(file):
    (V, L) = loadWeightedGraph(file)
    G = nx.Graph()
    for i in range(1, V + 1):
        G.add_node(i)
    
    for (u, v, _) in L:
        G.add_edge(u, v)
    
    return check_planarity(G)[0]


def test():
    areThereProblems = False
    graphs = listdir("graphs//planar")
    print (graphs)

    for graph in graphs:
        if not isfile("graphs/planar/" + graph):
            continue
        f = open("graphs/planar/" + graph, "r")
        ans = int(readSolution("graphs/planar/" + graph))
        print("============================")
        print("filename: " + graph)
        myans = planarity("graphs/planar/" + graph)
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
