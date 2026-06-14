def solution(n, wires):
    answer = -1
    adj = [[] for _ in range(n+1)]
    
    # 양방향 그래프 구성
    for u, v in wires:
        adj[u].append(v)
        adj[v].append(u)
    
    # cur: 현재 노드, p: 부모 노드 (역행 방지)
    # 현재 노드 기준 서브트리 크기 반환
    def dfs(cur, p):
        cnt = 1  # 자기 자신
        for nxt in adj[cur]:
            if nxt != p:  # 부모 방향으로 역행 방지
                cnt += dfs(nxt, cur)
        return cnt
    
    for i, (u, v) in enumerate(wires):
        # 간선 u-v 끊기
        adj[u].remove(v)
        adj[v].remove(u)
        
        size = dfs(1, -1)  # 1번 노드 기준 한쪽 크기
        diff = abs(size - (n - size))  # 두 그룹 크기 차이
        
        if i == 0:
            answer = diff  # 첫 번째 초기화 (-1 비교 방지)
        
        if diff == 0:
            answer = 0
            break  # 차이 0이면 최솟값이므로 즉시 종료
        else:
            answer = min(answer, diff)
        
        # 간선 복구
        adj[u].append(v)
        adj[v].append(u)
    
    return answer