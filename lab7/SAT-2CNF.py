import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dimacs import loadCNFFormula
from runtest import runtest
import networkx as nx
from networkx.algorithms.components import strongly_connected_components
from networkx.algorithms.dag import topological_sort


def sat2cnf(file):
    (V, F) = loadCNFFormula(file)
    G = nx.DiGraph()
    
    for i in range(1, V + 1):
        G.add_node(i)
        G.add_node(-i)
    
    for (u, v) in F:
        G.add_edge(-u, v)
        G.add_edge(-v, u)
    
    SCC = strongly_connected_components(G)
    
    H = nx.DiGraph()
    
    components = []
    vertices_bool = [None for _ in range(V + 1)]

    t = 0
    for S in SCC:
        for v in S:
            if -v in S:
                return False
            
        H.add_node(len(components))    
        components.append(S)
    
    for node in H.nodes:
        for origin in components[node]:
            for second_node in H.nodes:
                if node == second_node: continue
                if len(set(G[origin]) & components[second_node]) > 0:
                    H.add_edge(node, second_node)
 
    O = topological_sort(H)

    for v in O:
        for var in components[v]:
            if var > 0 and vertices_bool[var] is None:
                vertices_bool[var] = False
            if var < 0 and vertices_bool[-var] is None:
                vertices_bool[-var] = True
    print(vertices_bool)
    
    print("Is valuation correct: ", are_values_ok(F, vertices_bool))

    return True


def are_values_ok(G, B):
    for u, v in G:
        if u < 0 and v < 0 and (not (not B[-u] or not B[-v])):
            return False
        if u < 0 and v > 0 and (not (not B[-u] or B[v])):
            return False
        if u > 0 and v < 0 and (not (B[u] or not B[-v])):
            return False
        if u > 0 and v > 0 and (not (B[u] or B[v])):
            return False

    return True


graphs = os.path.dirname(os.path.abspath(__file__)) + "\\graphs\\sat"

runtest(sat2cnf, graphs)
