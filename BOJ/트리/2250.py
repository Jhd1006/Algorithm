import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
lc = [-1] * (N+1)
rc = [-1] * (N+1)
isRoot = [True] * (N+1)
isRoot[0] = False

for _ in range(N):
    n, l, r = map(int, input().split())
    lc[n] = l
    rc[n] = r
    if l != -1:
        isRoot[l] = False
    if r != -1:
        isRoot[r] = False
root = isRoot.index(True)

order = [[] for _ in range(N+1)]
num = 1
def inorder(cur, depth):
    global num
    if lc[cur] != -1:
        inorder(lc[cur], depth+1)
    order[depth].append(num)
    num += 1
    if rc[cur] != -1:
        inorder(rc[cur], depth+1)
inorder(root, 1)
mx = 0
for i in range(N+1):
    if order[i]:
        width = max(order[i]) - min(order[i]) + 1
        if mx < width:
            level = i
            mx = width
print(level, mx)
