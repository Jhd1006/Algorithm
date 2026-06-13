import heapq

def solution(operations):
    answer = []
    pq = []
    for op in operations:
        cmd, n = op.split()
        n = int(n)
        if cmd == 'I':
            heapq.heappush(pq, n)
        else:
            if pq:
                if n == 1:
                    mx = max(pq)
                    pq.remove(mx)
                elif n == -1:
                    heapq.heappop(pq)
    if pq:
        answer = [max(pq), pq[0]]
    else:
        answer = [0, 0]
    return answer
