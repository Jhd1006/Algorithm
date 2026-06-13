def solution(array, commands):
    answer = []
    for c in commands:
        i, j, k = c
        sliced_array = array[i-1:j]
        sorted_array = sorted(sliced_array)
        answer.append(sorted_array[k-1])
    return answer