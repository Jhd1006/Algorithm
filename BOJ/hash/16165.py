import sys
input = sys.stdin.readline

N, M = map(int, input().split())

team_to_mem = {}
mem_to_team = {}
ans = []

for _ in range(N):
    team = input().strip()
    num = int(input().strip())
    team_to_mem[team] = []
    for _ in range(num):
        mem = input().strip()
        team_to_mem[team].append(mem)
        mem_to_team[mem] = team
    team_to_mem[team].sort()

for _ in range(M):
    q_1 = input().strip()
    q_2 = int(input().strip())
    if q_2 == 0:
        for m in team_to_mem[q_1]:
            ans.append(m)
    elif q_2 == 1:
        ans.append(mem_to_team[q_1])

print('\n'.join(ans))

