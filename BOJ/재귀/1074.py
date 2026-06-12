import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

def z(x, y, n):
    if n == 0:
        return 0
    half = 1 << (n -1)
    val = half * half
    if x < half and y < half:
        return z(x, y, n-1)
    elif x < half and y >= half:
        return val + z(x, y - half, n-1)
    elif x >= half and y < half:
        return 2 * val + z(x-half, y, n-1)
    elif x >= half and y >= half:
        return 3 * val + z(x-half, y-half, n-1)

print(z(r, c, N))
