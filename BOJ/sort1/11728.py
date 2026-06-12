import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

merged = []
aidx = 0
bidx = 0
for i in range(0, N+M):
    if aidx == N:
        merged.append(B[bidx])
        bidx += 1
    elif bidx == M:
        merged.append(A[aidx])
        aidx += 1
    elif A[aidx] <= B[bidx]:
        merged.append(A[aidx])
        aidx += 1
    else:
        merged.append(B[bidx])
        bidx += 1
# merged = A+B
# merged.sort()

print(' '.join(map(str,merged)))
