def solution(cards):
    answer = 0
    n = len(cards)
    vis = [False] * n
    arr = []
    
    def card(start):
        idx = start
        cnt = 0
        while not vis[idx]:                
            vis[idx] = True
            cnt += 1
            idx = cards[idx] - 1
        return cnt
    
    for i in range(n):
        if vis[i]:
            continue
        arr.append(card(i))
    
    arr.sort(reverse = True)
    
    if len(arr) < 2:
        return 0
    else:
        answer = arr[0] * arr[1]
        
    return answer
