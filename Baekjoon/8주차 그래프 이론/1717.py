import sys

n, m = map(int, sys.stdin.readline().split())
lst = [[i] for i in range(n + 1)]

for _ in range(m):
    lst.append(list(map(int, sys.stdin.readline().split())))

for i in range(m):
    