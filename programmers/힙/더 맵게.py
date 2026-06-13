import heapq

def solution(scoville, K):
    heapq.heapify(scoville)  
    answer = 0
    while scoville:
        if scoville[0] >= K:
            break
        if len(scoville) < 2:
            return -1
        answer += 1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        mixed = first + second * 2
        heapq.heappush(scoville, mixed)
    return answer