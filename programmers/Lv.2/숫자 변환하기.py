from collections import deque

def solution(x, y, n):

    answer = 0
    if x == y:
        return 0
    vis = set()
    q = deque([(x, 0)])
    
    while q:
        cur, cnt = q.popleft()
        for nxt in [cur + n, cur * 2, cur * 3]:
            if nxt == y:
                answer = cnt + 1
                return answer
            if nxt <= y and nxt not in vis:
                vis.add(nxt)
                q.append((nxt, cnt + 1))
                
    answer = -1
    return answer
