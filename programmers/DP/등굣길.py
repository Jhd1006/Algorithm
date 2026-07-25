def solution(m, n, puddles):
    answer = 0
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for r in range(1, n + 1):
        for c in range(1, m + 1):
            if [c, r] in puddles:
                dp[r][c] = 0
            elif r == 1 and c == 1:
                dp[1][1] = 1
            elif r == 1:
                dp[r][c] = dp[r][c-1]
            elif c == 1:
                dp[r][c] = dp[r-1][c]
            else:
                dp[r][c] = (dp[r][c-1] + dp[r-1][c]) % 1000000007
    answer = dp[n][m]
    return answer
