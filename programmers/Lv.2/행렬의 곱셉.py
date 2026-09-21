def solution(arr1, arr2):
    answer = [[]]
    row1 = len(arr1)
    col1 = len(arr1[0])
    col2 = len(arr2[0])
    answer = [[0] * col2 for _ in range(row1)]  

    for i in range(row1):
        for j in range(col1):
            for k in range(col2):
                answer[i][k] += arr1[i][j] * arr2[j][k]

    return answer
