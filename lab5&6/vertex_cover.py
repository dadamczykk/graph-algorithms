import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from runtest import runtest
from lex_BFS import lex_BFS, read_graph


def vertex_cover(graph):
    G = read_graph(graph)
    visited, _, _ = lex_BFS(G)
    I = set()
    visited = visited[::-1]
    
    for v in visited:
        if G[v].out & I == set():
            I.add(v)
    out = set(visited)
    return len(out - I)


graphs = os.path.dirname(os.path.abspath(__file__)) + "\\graphs\\vcover"

runtest(vertex_cover, graphs)
