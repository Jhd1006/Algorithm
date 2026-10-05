import heapq

def solution(n, k, enemy):
    answer = 0
    pq = []
    
    answer = len(enemy)
    
    for i, e in enumerate(enemy):
        heapq.heappush(pq, e)
        if len(pq) > k:
            cur = heapq.heappop(pq)
            n -= cur
            if n < 0:
                return i

    return answer
