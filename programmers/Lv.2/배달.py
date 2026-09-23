import heapq

def solution(N, road, K):
    answer = 0
    adj = [[] for _ in range(N + 1)]
    inf = float('inf')
    d = [inf] * (N + 1)
    
    for u, v, w in road:
        adj[u].append((w, v))
        adj[v].append((w, u))
    
    pq = []
    d[1] = 0
    heapq.heappush(pq, (d[1], 1))
    
    while pq:
        dist, node = heapq.heappop(pq)
        if dist > d[node]:
            continue
        for nxt_dist, nxt_node in adj[node]:
            if d[node] + nxt_dist >= d[nxt_node]:
                continue
            d[nxt_node] = d[node] + nxt_dist
            heapq.heappush(pq, (d[nxt_node], nxt_node))
            
    answer = sum(x <= K for x in d)
    return answer
