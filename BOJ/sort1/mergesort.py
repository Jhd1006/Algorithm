arr1 = [-9, 1, 6, 8, 12]
arr2 = [-7, 7, 13, 15]
new_arr = []
idx_1 = 0
idx_2 = 0
for i in range(5+4):
    if idx_1 == 5:
        new_arr.append(arr2[idx_2])
        idx_2 += 1
    elif idx_2 == 4:
        new_arr.append(arr1[idx_1])
        idx_1 += 1
    elif arr1[idx_1] <= arr2[idx_2]:
        new_arr.append(arr1[idx_1])
        idx_1 += 1
    else:
        new_arr.append(arr2[idx_2])
        idx_2 += 1
print(new_arr)