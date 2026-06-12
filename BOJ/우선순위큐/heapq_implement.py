import sys 
input = sys.stdin.readline

heap = [0] * 100005
sz = 0; # heap에 들어있는 원소의 수

def push(x):
    global sz
    sz += 1
    heap[sz] = x
    idx = sz
    while idx != 1:
        par = idx // 2
        if heap[par] < heap[idx]:
            break
        heap[par], heap[idx] = heap[idx], heap[par]
        idx = par

def top():
    return heap[1]


def pop():
    global sz
    heap[1] = heap[sz]
    sz -= 1
    idx = 1
    while (2*idx) <= sz:
        lc = 2 * idx
        rc = (2 * idx) + 1
        min_child = lc
        if rc <= sz and heap[rc] < heap[lc]:
            min_child = rc
        if heap[idx] <= heap[min_child]:
            break
        heap[idx], heap[min_child] = heap[min_child], heap[idx]
        idx = min_child

def test():
    push(10)
    push(2)
    push(5)
    push(9)
    print(top()) # 2
    pop()
    pop()
    print(top()) # 9
    push(5)
    push(15)
    print(top()) # 5
    pop()
    print(top()) # 9
#   push(10); push(2); push(5); push(9); // {10, 2, 5, 9}
#   cout << top() << '\n'; // 2
#   pop(); // {10, 5, 9}
#   pop(); // {10, 9}
#   cout << top() << '\n'; // 9
#   push(5); push(15); // {10, 9, 5, 15}
#   cout << top() << '\n'; // 5
#   pop(); // {10, 9, 15}
#   cout << top() << '\n'; // 9


test()