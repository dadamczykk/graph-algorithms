import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from runtest import runtest
from lex_BFS import lex_BFS, read_graph


def vertex_coloring(graph):
    G = read_graph(graph)
    visited, _, _ = lex_BFS(G)
    vertex_color = [0 for _ in range(len(G))]

    for v in visited:
        neighbours_colors = set([vertex_color[c] for c in G[v].out])
        color = 1

        while True:
            if color not in neighbours_colors:
                vertex_color[v] = color
                break

            color += 1

    return max(vertex_color)


graphs = os.path.dirname(os.path.abspath(__file__)) + "\\graphs\\coloring"

runtest(vertex_coloring, graphs)
