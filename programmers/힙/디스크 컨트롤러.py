import heapq

def solution(jobs):
    answer = 0
    time = 0
    tot = 0
    i = 0
    waiting = []
    jobs.sort()
    while i < len(jobs) or waiting:
        while i < len(jobs) and jobs[i][0] <= time:
            start, duration = jobs[i]
            heapq.heappush(waiting, [duration, start])
            i += 1
        if waiting:
            d, s = heapq.heappop(waiting)
            time += d
            tot += time - s
        else:
            time = jobs[i][0]
    answer = tot // len(jobs)
    return answer

# 대기 큐 (번호, 요청 시각, 소요 시간)
# 작업 안하고 있고, 대기큐 안비어 있으면 (소요시간, 요청 시각, 번호 순)
# 한번에 하나의 작업만