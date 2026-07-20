# 코드 2 => 코드 1의 bfs 여러번 수행되는 점 개선 (q에 시작점 한번에 넣음)
# 코드 3 => begin 노드를 추가하여 초기화로직도 bfs와 합침
# 코드 4 => (단어, 거리)를 큐에 함께 넣어 dist 배열 없이 처리

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

# from collections import deque

# def solution(begin, target, words):
#     answer = 0
#     dist = [-1] * len(words)
    
#     def is_similar(a, b):
#         cnt = 0
#         l = len(a)
#         for i in range(l):
#             if a[i] != b[i]:
#                 cnt += 1
#                 if cnt > 1:
#                     return False
#         return True
    
#     if target not in words:
#         return 0
    
#     q = deque()
#     for i in range(len(words)):
#         if is_similar(words[i], begin):
#             q.append(i)
#             dist[i] = 1

#     while q:
#         cur = q.popleft()     
#         if words[cur] == target:
#             return dist[cur]       
#         for nxt in range(len(words)):
#             if dist[nxt] != -1 or not is_similar(words[cur], words[nxt]):
#                 continue
#             dist[nxt] = dist[cur] + 1
#             q.append(nxt)
    
# #     return answer

# from collections import deque

# def solution(begin, target, words):
#     answer = 0
#     length = len(words)
    
#     def is_similar(a, b):
#         cnt = 0
#         l = len(a)
#         for i in range(l):
#             if a[i] != b[i]:
#                 cnt += 1
#                 if cnt > 1:
#                     return False
#         return True
    
#     words.append(begin)
#     dist = [-1] * len(words)
#     q = deque([-1])
#     dist[-1] = 0
    
#     while q:
#         cur = q.popleft()
#         if words[cur] == target:
#             answer = dist[cur]
#             break
#         for nxt in range(length):
#             if is_similar(words[cur], words[nxt]) and dist[nxt] == -1:
#                 dist[nxt] = dist[cur] + 1
#                 q.append(nxt)
#     return answer


from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque([(begin, 0)])
    vis = [False] * len(words)
    
    while q:
        cur, cnt = q.popleft()
        if cur == target:
            answer = cnt
            break
        for idx, word in enumerate(words):
            if vis[idx]:
                continue
            if sum(a != b for a, b in zip(cur, word)) < 2:
                vis[idx] = True
                q.append((word, cnt + 1))
    return answer
