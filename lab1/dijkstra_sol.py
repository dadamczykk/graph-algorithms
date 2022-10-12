from dimacs import loadWeightedGraph, readSolution
from os import listdir
from os.path import isfile
from queue import PriorityQueue


def makeAdjList(V, L):
    R = [[] for _ in range(V)]
    for el in L:
        R[el[0]].append([el[1], el[2]])
        R[el[1]].append([el[0], el[2]])
    return R


def sol(A):
    (V, L) = loadWeightedGraph(A)
    V += 1
    s, t = 1, 2
    q = PriorityQueue()
    weight = [float("-inf") for _ in range(V)]
    weight[s] = float("inf")
    G = makeAdjList(V, L)
    q.put((float("inf"), s))
    while not q.empty():
        wi, v = q.get()
        if v == t:
            return -wi
        if weight[v] > -wi and weight[v] != float("inf"):
            continue
        for u in G[v]:
            if weight[v] >= u[1] and weight[u[0]] < u[1]:
                weight[u[0]] = u[1]
                q.put((-u[1], u[0]))
            if weight[v] <= u[1] and weight[u[0]] < weight[v]:
                weight[u[0]] = weight[v]
                q.put((-weight[v], u[0]))

    return weight[t]


graphs = listdir("graphs")

for graph in graphs:
    if not isfile("graphs/" + graph):
        continue
    f = open("graphs/" + graph, "r")
    line = f.readline()
    ans = int(readSolution("graphs/" + graph))
    myans = sol("graphs/" + graph)
    print("============================")
    print("filename: " + graph)
    print("given solution: ", ans)
    print("my solution: ", myans)
    print("answer is " + "correct" if myans == ans else "uncorrect")
