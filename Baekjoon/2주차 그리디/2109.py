import sys

n = int(sys.stdin.readline())
lst = []
money = 0
cnt = 0

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    lst.append([a, b])

lst = sorted(lst, key = lambda x : (x[1], -x[0]))

for i in range(n):
    if cnt != lst[i][1]:
        money += lst[i][0]
        cnt += 1
print(money)