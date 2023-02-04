# Greedy solution

from data import runtests
from queue import PriorityQueue

def my_solve(N, M, K, base, wages, eqCost):
    queue = PriorityQueue()

    for i in range(N):
        for p in range(len(wages[i])):
            wages[i][p] = wages[i][p][1] + eqCost[wages[i][p][0] - 1]
        wages[i].sort()

        for _ in range(len(wages[i])-len(base[i])):
            wages[i].pop()

        wages[i][0] += base[i][0]

        for a in range(1, min(len(base[i]), len(wages[i]))):
            wages[i][a] += base[i][a] - base[i][a-1]

        wages[i].reverse()
        queue.put((wages[i][-1], i))
    
    cost = 0
    for _ in range(K):
        toAdd, toInsPop = queue.get()
        cost += toAdd
        wages[toInsPop].pop()
        if len(wages[toInsPop]) != 0:
            queue.put((wages[toInsPop][-1], toInsPop))

    return cost

runtests(my_solve)
