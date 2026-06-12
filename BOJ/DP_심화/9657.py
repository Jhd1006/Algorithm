import sys
input = sys.stdin.readline


N = int(input())

def game(N):
    if N <= 4:
        if N == 2:
            return 2
        else:
            return 1
    else:
        dp = [0] * (N+1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 1
        dp[4] = 1       
        for i in range(5, N+1):
            if dp[i-1] == 2 or dp[i-3] == 2 or dp[i-4] == 2:
                dp[i] = 1
            else:
                dp[i] = 2
        return dp[N]

print("SK" if game(N) == 1 else "CY")


