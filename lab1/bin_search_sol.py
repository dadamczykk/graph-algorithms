from collections import deque
from dimacs import loadWeightedGraph, readSolution
from os import listdir
from os.path import isfile

# DFS solution requires changing recursion depth limit, or implementation of stack

def makeAdjList(V, L):
    R = [[] for _ in range(V)]
    for el in L:
        R[el[0]-1].append([el[1]-1, el[2]])
        R[el[1]-1].append([el[0]-1, el[2]])
    return R

def DFS(G, s, t, cap):
    V = len(G)
    visited = [False for _ in range(V)]
    visited[s] = True
    
    def dfs_visit(G, u):
        nonlocal cap
        visited[u] = True
        for v, val in G[u]:
            if not visited[v] and val > cap:
                dfs_visit(G, v)
    
    dfs_visit(G, s)
    
    return visited[t]

def BFS(G, s, t, cap):
    V = len(G)
    visited = [False for _ in range(V)]
    visited[s] = True
    q = deque()
    q.append(s)
    while q:
        u = q.popleft()
        for v, val in G[u]:
            if v == t and val > cap:
                return True
            if not visited[v] and val > cap:
                visited[v] = True
                q.append(v)
    return visited[t]


def binSearch(G, L, l, r, s, t):
    if r >= l:
        mid = l + (r - l) // 2
        if BFS(G, s, t, L[mid][2]):
            return binSearch(G, L, mid + 1, r, s, t)
        else:
            return binSearch(G, L, l, mid - 1, s, t)
    else:
        return L[l][2]
    
def sol(A):
    (V, L) = loadWeightedGraph(A)
    G = makeAdjList(V, L)
    s, t = 0, 1
    L.sort(key=lambda x : x[2])
    return binSearch(G, L, 0, len(L) - 1, s, t)
    

graphs = listdir("graphs")

for graph in graphs:
    # if graph != "path10":
    #     continue
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
