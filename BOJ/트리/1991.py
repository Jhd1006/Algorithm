import sys
input = sys.stdin.readline

preans = []
postans = []
inans = []

def preorder(cur):
    preans.append(chr(cur + ord('A') - 1))
    if lc[cur] != 0:
        preorder(lc[cur])
    if rc[cur] != 0:
        preorder(rc[cur])

def inorder(cur):
    if lc[cur] != 0:
        inorder(lc[cur])
    inans.append(chr(cur + ord('A') - 1))
    if rc[cur] != 0:
        inorder(rc[cur])

def postorder(cur):
    if lc[cur] != 0:
        postorder(lc[cur])
    if rc[cur] != 0:
        postorder(rc[cur])
    postans.append(chr(cur + ord('A') - 1))
    

N = int(input())
lc = [0] * (N+1)
rc = [0] * (N+1)

for _ in range(N):
    m, l, r = input().split()
    if l != '.':
        lc[ord(m) - ord('A') + 1] = ord(l) - ord('A') + 1
    if r != '.':
        rc[ord(m) - ord('A') + 1] = ord(r) - ord('A') + 1

preorder(1)
inorder(1)
postorder(1)

print(''.join(preans))
print(''.join(inans))
print(''.join(postans))

    
