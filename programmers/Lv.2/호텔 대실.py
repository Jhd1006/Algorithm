import heapq

def solution(book_time):
    answer = 0
    pq = []
    
    def time(t):
        h, m = map(int, t.split(':'))
        return h * 60 + m
    
    times = [(time(start), time(end) + 10) for start, end in book_time]
    times.sort()
    
    for start, end in times:
        if pq and pq[0] <= start:
            heapq.heappop(pq)
        heapq.heappush(pq, end)
    
    answer = len(pq)

    return answer
