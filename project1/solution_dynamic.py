# Dynamic programming solution

from data import runtests

def my_solve(N, M, K, base, wages, eqCost):
    
    for i in range(N):
        for p in range(len(wages[i])):
            wages[i][p] = wages[i][p][1] + eqCost[wages[i][p][0] - 1]
            
        wages[i].sort()

        for _ in range(len(wages[i])-len(base[i])):
            wages[i].pop()

        wages[i][0] += base[i][0]

        for a in range(1, len(wages[i])):
    
            wages[i][a] += base[i][a] - base[i][a-1] + wages[i][a-1]
    
    lengths = [0 for _ in range(N)]
    lengths[0] = len(wages[i])
    
    for i in range(1,N):
        lengths[i] = lengths[i-1] + len(wages[i])

    DP = [[float("inf") for _ in range(K)] for _ in range(N)]
    
    for i in range(len(wages[0])):
        DP[0][i] = wages[0][i]

    for i in range(1, N):
        DP[i][0] = min(wages[i][0], DP[i-1][0])

    for i in range(1, N):
        for k in range(1, min(K, lengths[i])):
            if k < len(wages[i]):
                DP[i][k] = wages[i][k]
            for k2 in range(0, k):
                if len(wages[i]) > k - k2 - 1:
                    DP[i][k] = min(DP[i][k], DP[i-1][k2] + wages[i][k - k2 - 1])
            DP[i][k] = min(DP[i][k], DP[i-1][k])

    return DP[-1][-1]


runtests(my_solve)
