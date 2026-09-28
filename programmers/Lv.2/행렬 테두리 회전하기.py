def solution(rows, columns, queries):
    answer = []
    arr = [[0] * columns for _ in range(rows)]
    
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = i * columns + j + 1
            
    for q in queries:
        x1, y1, x2, y2 = [num - 1 for num in q]
        tmp = arr[x1][y1]
        mn = tmp
        
        for i in range(x1, x2):
            arr[i][y1] = arr[i + 1][y1]
            mn = min(mn, arr[i][y1])
        for i in range(y1 , y2):
            arr[x2][i] = arr[x2][i+1]
            mn = min(mn, arr[x2][i])
        for i in range(x2, x1, -1):
            arr[i][y2] = arr[i-1][y2]
            mn = min(mn, arr[i][y2])
        for i in range(y2, y1 + 1, -1):
            arr[x1][i] = arr[x1][i -1]
            mn = min(mn, arr[x1][i])
        arr[x1][y1+1] = tmp
        answer.append(mn)

    return answer
