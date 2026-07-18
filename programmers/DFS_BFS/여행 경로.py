def solution(tickets):
    answer = []
    l = len(tickets)
    tickets.sort()
    vis = [False] * l
    def dfs(cur, path):
        if len(path) == l + 1:
            answer.append(path) 
            return
        for idx, ticket in enumerate(tickets):
            if vis[idx] or ticket[0] != cur:
                continue
            vis[idx] = True
            dfs(ticket[1], path + [ticket[1]])
            vis[idx] = False
    dfs('ICN', ['ICN'])
    answer = answer[0]
    return answer

def solution(tickets):
    answer = []
    l = len(tickets)
    tickets.sort()
    vis = [False] * l
    def dfs(cur, path):
        if len(path) == l + 1:
            answer.append(path) 
            return True
        for idx, ticket in enumerate(tickets):
            if vis[idx] or ticket[0] != cur:
                continue
            vis[idx] = True
            if dfs(ticket[1], path + [ticket[1]]):         # 더 깊은 곳의 dfs가 True를 반환하면, dfs 연쇄적으로 True 반환하며 조기 종료
                return True
            vis[idx] = False
    dfs('ICN', ['ICN'])
    answer = answer[0]
    return answer
