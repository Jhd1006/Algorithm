# import sys
# input = sys.stdin.readline

# K = int(input().strip())
# ans = []
# def hanoi(k, start, other, end):
#     if k == 1:
#         ans.append((start, end))
#         return
#     hanoi(k-1, start, end, other)
#     ans.append((start, end))
#     hanoi(k-1, other, start, end)

# hanoi(K, 1, 2, 3)
# print(len(ans))
# for a, b in ans:
#     print(a,b)


# # start, other, end
# ans.append(start, end) 가 +1 역할
# # - 
# # --
# # --
# # ----
# hanoi(K, start, end, other)
# #      -
# #      --
# # ---- ---  
# hanoi(K, other, end, start)
# #            -
# #            --  
# #            ---
# #            ----


import sys
input = sys.stdin.readline

K = int(input().strip())
ans = []

def hanoi(k, start, end, other):
    if k == 1:
        ans.append((start, end))
        return
    hanoi(k-1, start, other, end)
    ans.append((start, end))
    hanoi(k-1, other, end, start)


hanoi(K, 1, 3, 2)
print(len(ans))
for a, b in ans:
    print(a, b)
    



    




