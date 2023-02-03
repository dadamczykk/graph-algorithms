import networkx as nx
from genericpath import isfile
from os import listdir
from networkx.algorithms.components import strongly_connected_components
from networkx.algorithms.dag import topological_sort
from dimacs import loadCNFFormula, readSolution


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
    
    print("Czy wartościowanie jest poprawne: ", are_values_ok(F, vertices_bool))

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


def test():
    areThereProblems = False
    graphs = listdir("graphs//sat")
    print (graphs)

    for graph in graphs:
        if not isfile("graphs/sat/" + graph):
            continue
        f = open("graphs/sat/" + graph, "r")
        ans = int(readSolution("graphs/sat/" + graph))
        print("============================")
        print("filename: " + graph)
        myans = sat2cnf("graphs/sat/" + graph)
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