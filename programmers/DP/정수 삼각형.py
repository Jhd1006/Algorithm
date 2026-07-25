# def solution(triangle):
#     answer = 0
#     l = len(triangle)
#     dp = [[0] * l for _ in range(l)]
#     for i in range(l):
#         for j in range(i + 1):
#             dp[i][j] = triangle[i][j]
#     for i in range(1, l):
#         for j in range(0, i + 1):
#             if j == 0:
#                 dp[i][j] = dp[i-1][j] + dp[i][j]
#             elif j == i:
#                 dp[i][j] = dp[i-1][j-1] + dp[i][j]
#             else:
#                 dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + dp[i][j]
#     answer = max(dp[l-1])
#     return answer

def solution(triangle):
    answer = 0
    l = len(triangle)
    dp = [row[:] for row in triangle]
    for i in range(l - 2, -1, -1):
        for j in range(i + 1):
                dp[i][j] += max(dp[i+1][j], dp[i+1][j+1])
    answer = dp[0][0]
    return answer

# dp 누적합 시 맨 아래의 행부터 거꾸로 올라가면, 분기를 통해 양끝 칸의 예외처리 코드를 작성할 필요가 없어짐
