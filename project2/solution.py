from data import runtests

def my_solve(N, channels):
    
    if len(channels) == 0 and N == 0:
        return None
    
    elif len(channels) == 0:
        return 1
    
    G = [(set(), i) for i in range(N+1)]
    H = G.copy()
    
    for ch0, ch1 in channels:
        G[ch0][0].add(ch1)
        G[ch1][0].add(ch0)
    
    G.sort(key = lambda x : len(x[0]), reverse=True)
    
    clique = (G[0][0] | {G[0][1]})
    i = 1
    
    while len(clique) > i:
        clique = clique & (G[i][0] | {G[i][1]})
        i+=1
    
    if i != len(clique):
        return None
    
    for node in H[i:]:
        if node[1] not in clique and len(node[0] - clique) != 0:
            return None
        
    cl = list(clique)    
    
    for i in cl:
        if len(H[i][0] - clique) == 0:
            return len(clique) - 1
    
    return len(clique)

    return 0

runtests(my_solve)
