# from collections import deque
# def solution(begin, target, words):
#     answer = 0
#     dist = [-1] * len(words)
#     def is_similar(begin, word):
#         cnt = 0
#         l = len(begin)
#         for i in range(l):
#             if begin[i] != word[i]:
#                 cnt += 1
#                 if cnt > 1 :
#                     return False
#         return True
    
#     def bfs(start):
#         q = deque([start])
#         dist[start] = 1
#         while q:
#             cur = q.popleft()
#             for nxt in range(len(words)):
#                 if dist[nxt] != -1:
#                     continue
#                 if not is_similar(words[cur], words[nxt]):
#                     continue
#                 print(words[nxt])
#                 q.append(nxt)
#                 dist[nxt] = dist[cur] + 1
           
#     if target in words:
#         for i in range(len(words)):
#             if is_similar(begin, words[i]):
#                 bfs(i)
#         idx = words.index(target)
#         answer = dist[idx]
#     return answer 

from collections import deque

def solution(begin, target, words):
    answer = 0
    dist = [-1] * len(words)
    
    def is_similar(a, b):
        cnt = 0
        l = len(a)
        for i in range(l):
            if a[i] != b[i]:
                cnt += 1
                if cnt > 1:
                    return False
        return True
    
    if target not in words:
        return 0
    
    q = deque()
    for i in range(len(words)):
        if is_similar(words[i], begin):
            q.append(i)
            dist[i] = 1

    while q:
        cur = q.popleft()     
        if words[cur] == target:
            return dist[cur]       
        for nxt in range(len(words)):
            if dist[nxt] != -1 or not is_similar(words[cur], words[nxt]):
                continue
            dist[nxt] = dist[cur] + 1
            q.append(nxt)
    
    return answer
