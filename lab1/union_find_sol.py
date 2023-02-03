import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dimacs import loadWeightedGraph
from runtest import runtest

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

graphs = os.path.dirname(os.path.abspath(__file__)) + "\\graphs"

runtest(sol, graphs)
