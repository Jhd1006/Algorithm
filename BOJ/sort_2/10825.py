import sys
input = sys.stdin.readline

N = int(input())

arr = []

def sorting(a):
    return (-int(a[1]), int(a[2]), -int(a[3]), a[0])
for _ in range(N):
    name, kor, eng, math = input().split()
    arr.append((name, kor, eng, math))
arr.sort(key=sorting)

for a in arr:
    print(a[0])
    
# 12
# Junkyu 50 60 100
# Sangkeun 80 60 50
# Sunyoung 80 70 100
# Soong 50 60 90
# Haebin 50 60 100
# Kangsoo 60 80 100
# Donghyuk 80 60 100
# Sei 70 70 70
# Wonseob 70 70 90
# Sanghyun 70 70 80
# nsj 80 80 80
# Taewhan 50 60 90

# Donghyuk
# Sangkeun
# Sunyoung
# nsj
# Wonseob
# Sanghyun
# Sei
# Kangsoo
# Haebin
# Junkyu
# Soong
# Taewhan