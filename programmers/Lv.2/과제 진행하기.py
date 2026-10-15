def solution(plans):
    answer = []
    plans.sort(key = lambda x : x[1])
    stack = []
    
    def into_min(start):
        st = start.split(':')
        minute = int(st[0]) * 60 + int(st[1])
        return minute

    for i in range(len(plans)):
        name, start, playtime = plans[i]
        start = into_min(start)
        playtime = int(playtime)
        plans[i] = [name, start, playtime]

    for i in range(len(plans) - 1):
        name, start, playtime = plans[i]
        nxt = plans[i + 1]
        if start + playtime <= nxt[1]:
            answer.append(name)
            extra = nxt[1] - (start + playtime)
            while stack and extra > 0:
                prev = stack.pop()
                if prev[2] <= extra:
                    answer.append(prev[0])
                    extra -= prev[2]
                else:
                    prev[2] -= extra
                    stack.append([prev[0], prev[1], prev[2]])
                    extra = 0
        else:
            stack.append([name, start, playtime - (nxt[1] - start)])
    
    answer.append(plans[-1][0])

    while stack:
        stop = stack.pop()
        answer.append(stop[0])
                    
    return answer
