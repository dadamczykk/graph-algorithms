import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dimacs import loadWeightedGraph
from runtest import runtest
import networkx as nx
from networkx.algorithms.planarity import check_planarity


def planarity(file):
    (V, L) = loadWeightedGraph(file)
    G = nx.Graph()
    for i in range(1, V + 1):
        G.add_node(i)
    
    for (u, v, _) in L:
        G.add_edge(u, v)
    
    return check_planarity(G)[0]

graphs = os.path.dirname(os.path.abspath(__file__)) + "\\graphs\\planar"

runtest(planarity, graphs)
