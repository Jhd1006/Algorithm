def solution(money):
    answer = 0
    n = len(money)
    dp1 = [0] * n
    dp2 = [0] * n
    
    # 첫번째 집을 고름 => 마지막 집 못고르니, 마지막-1번째 집까지
    for i in range(n-1):
        if i < 2:
            dp1[i] = money[i]
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
    
    # 첫번째 집 안고름 => 마지막 집 선택 가능
    for i in range(1, n):
        if i == 1:
            dp2[i] = money[i]
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])  
        
    answer = max(dp1[n-2], dp2[n-1])
    return answer


# MONEY 배열에서 슬라이싱으로 첫번째 집 고른 것과 마지막집 고른 것 분리 => 이후 한번에 함수에 넣기
  
# def solution(money):
#     answer = 0
#     def dp_linear(arr):
#         dp = [0] * len(arr)
#         dp[0] = arr[0]
#         dp[1] = max(arr[0], arr[1])
#         for i in range(2, len(arr)):
#             dp[i] = max(dp[i-1], dp[i-2] + arr[i])
#         return dp[-1]
    
#     select_first = money[:-1]
#     select_last = money[1:]
    
#     answer = max(dp_linear(select_first), dp_linear(select_last))
#     return answer
