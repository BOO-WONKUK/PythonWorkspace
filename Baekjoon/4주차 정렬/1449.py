import sys

n, l = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

start = lst[0]
end = lst[0] + l
cnt = 1
for i in range(n):
    if start <= lst[i] < end:
        continue
    else:
        start = lst[i]
        end = lst[i] + l
        cnt += 1
print(cnt)