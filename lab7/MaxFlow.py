import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dimacs import loadDirectedWeightedGraph
from runtest import runtest
import networkx as nx
from networkx.algorithms.flow import *


def flow(file):
    
    (V, L) = loadDirectedWeightedGraph(file)

    G = nx.DiGraph()
    
    for i in range(1, V + 1):
        G.add_node(i)
    
    for (u, v, t) in L:
        G.add_edge(u, v)
        G[u][v]['capacity'] = t

    return maximum_flow(G, 1, V)[0]


graphs = os.path.dirname(os.path.abspath(__file__)) + "\\graphs\\flow"

runtest(flow, graphs)