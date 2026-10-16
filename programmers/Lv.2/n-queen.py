# def solution(n):
#     answer = 0
#     isused = [False] * n
#     isused2 = [False] * (2 * n - 1)
#     isused3 = [False] * (2 * n - 1)
    
#     def nqueen(cur):
#         nonlocal answer
#         if cur == n:
#             answer += 1
#             return
#         for i in range(n):
#             if isused[i] or isused2[cur + i] or isused3[cur - i + n - 1]:
#                 continue
#             isused[i] = True
#             isused2[cur + i] = True
#             isused3[cur - i + n - 1] = True
#             nqueen(cur + 1)
#             isused[i] = False
#             isused2[cur + i] = False
#             isused3[cur - i + n - 1] = False
#     nqueen(0)
#     return answer

# ========== 변수 정리 nonlocal 제거 ==========
def solution(n):
    answer = 0
    cols = [False] * n
    diag1 = [False] * (2 * n -1)
    diag2 = [False] * (2 * n -1)
    
    def nqueen(row):
        if row == n:
            return 1
        cnt = 0
        for i in range(n):
            if cols[i] or diag1[row + i] or diag2[row - i + (n -1)]:
                continue
            cols[i] = True
            diag1[row + i] = True
            diag2[row - i + (n - 1)] = True
            
            cnt +=  nqueen(row + 1)
            cols[i] = False
            diag1[row + i] = False
            diag2[row - i + (n - 1)] = False
        return cnt
    
    answer = nqueen(0)
    return answer
