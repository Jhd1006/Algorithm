import sys
input = sys.stdin.readline

def bottom_up_fibo(n):
	f = [0] * (n+1)
	f[0] = f[1] = 1
	for i in range(2, n+1):
		f[i] = f[i-1]+ f[i-2]
	return f[n]

N = int(input())

print(bottom_up_fibo(N))

f = [-1] * (N+1)

def top_down_fibo(n):
	if f[n] != -1:
		return f[n]
	if n <= 1:
		f[n] = 1
		return f[n]
	f[n] = top_down_fibo(n-1) + top_down_fibo(n-2)
	return f[n]

print(top_down_fibo(N))
