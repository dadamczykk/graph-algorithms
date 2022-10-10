from dimacs import loadWeightedGraph, readSolution
from os import listdir
from os.path import isfile


class Node():
    def __init__(self, value):
        self.parent = self
        self.value = value
        self.rank = 0

    def find(self):
        if self.parent != self:
            self.parent = self.parent.find()
        return self.parent

    def union(self, y):
        self = self.find()
        y = y.find()
        if self == y: return
        if self.rank > y.rank:
            y.parent = self
        else:
            self.parent = y
            if self.rank == y.rank:
                y.rank += 1

def sol(A):
    (V, L) = loadWeightedGraph(A)
    L.sort(key=lambda x : x[2],reverse=True)
    forest = []
    for i in range(V + 1):
        forest.append(Node(i))
    s, t = 1, 2
    for el in L:
        if forest[el[0]].find() == forest[el[1]].find():
            continue
        forest[el[0]].union(forest[el[1]])
        if forest[s].find() == forest[t].find():
            return el[2]
    return None

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
