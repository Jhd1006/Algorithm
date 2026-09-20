def solution(arr):
    answer = -1
    l = len(arr)
    nums = [int(arr[i]) for i in range(0, l, 2)]
    ops = [arr[i] for i in range(1, l, 2)]
    n = len(nums)

    INF = float('inf')
    dp_max = [[-INF] * n for _ in range(n)] 
    dp_min = [[INF] * n for _ in range(n)]
    
    for i in range(n):
        dp_max[i][i] = nums[i]
        dp_min[i][i] = nums[i]
    
    for length in range(2, n+1):
        for st in range(n - length + 1):
            end = st + length - 1
            for i in range(st, end):
                op = ops[i]
                if op == '+':
                    mx = dp_max[st][i] + dp_max[i+1][end]
                    mn = dp_min[st][i] + dp_min[i+1][end]
                else:
                    mx = dp_max[st][i] - dp_max[i+1][end]
                    mn = dp_min[st][i] - dp_min[i+1][end]
                dp_max[st][end] = max(dp_max[st][end], mx)
                dp_min[st][end] = min(dp_min[st][end], mn)
                
    answer = dp_max[0][n-1]
    return answer
