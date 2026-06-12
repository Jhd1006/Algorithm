import sys
input = sys.stdin.readline

side, walk = map(int, input().split())

def pw(side, walk):
    if side == 2:
        if walk == 1:
            return 1, 1
        elif walk == 2:
            return 1, 2
        elif walk == 3:
            return 2, 2
        else:
            return 2, 1
    half = side // 2
    sq = half*half
    if walk <= sq:
        x, y = pw(half, walk)
        return y, x
    elif walk <= 2*sq:
        x, y = pw(half, walk - sq)
        return x, y + half
    elif walk <= 3*sq:
        x, y = pw(half, walk - 2*sq)
        return x + half, y + half
    elif walk <= 4*sq:
        x, y = pw(half, walk - 3*sq)
        return 2*half - y + 1, half - x + 1

print(' '.join(map(str, pw(side, walk))))