import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from runtest import runtest
from lex_BFS import lex_BFS, read_graph


def maximal_clique(graph):
    G = read_graph(graph)
    visited, right_neighbours, _ = lex_BFS(G)
    output = 0
    for vertex in visited:
        output = max(output, len(right_neighbours[vertex]) + 1)
    return output


graphs = os.path.dirname(os.path.abspath(__file__)) + "\\graphs\\maxclique"

runtest(maximal_clique, graphs)
