import collections

def bfs(graphMatrix, graphAdjList, s, t, parent):
    visited = [False] * len(graphAdjList)
    queue = collections.deque()
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.popleft()
        for el in graphAdjList[u]:
            if (visited[el] == False) and (graphMatrix[u][el] > 0):
                queue.append(el)
                visited[el] = True
                parent[el] = u
    return visited[t]


def dfs(graphMatrix, graphAdjList, s, t, parent):
    n = len(graphMatrix)
    visited = [False for _ in range(n)]
    def dfsVisit(graphMatrixDFS, u):
        nonlocal graphAdjList
        visited[u] = True
        for v in graphAdjList[u]:
            if graphMatrixDFS[u][v] > 0 and not visited[v]:
                parent[v] = u
                dfsVisit(graphMatrixDFS, v)
    dfsVisit(graphMatrix, s)
    return visited[t]


def edmondsKarp(graphMatrix, graphAdjList, source, sink):
    parent = [-1] * len(graphMatrix)
    max_flow = 0
    while bfs(graphMatrix, graphAdjList, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graphMatrix[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graphMatrix[u][v] -= path_flow
            graphMatrix[v][u] += path_flow
            v = parent[v]
    return max_flow