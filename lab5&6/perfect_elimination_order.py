import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from runtest import runtest
from lex_BFS import lex_BFS, read_graph


def check_PEO(visited, RN, parent):
    for v in visited:
        if parent[v] is not None and  not RN[v] <= RN[parent[v]] | {parent[v]}:
            return False
    return True


def perfect_elimination_order(graph):
    G = read_graph(graph)
    visited, right_neighbours, parents = lex_BFS(G)
    return check_PEO(visited, right_neighbours, parents)


graphs = os.path.dirname(os.path.abspath(__file__)) + "\\graphs\\chordal"

runtest(perfect_elimination_order, graphs)
