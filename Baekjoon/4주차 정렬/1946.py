import sys

t = int(sys.stdin.readline())
lst = []

for i in range(t):
    n = int(sys.stdin.readline())
    for j in range(n):
        a, b = map(int, sys.stdin.readline().split())
        lst.append([a,b])

    lst = sorted(lst, key = lambda x : x[0])
    cnt = 1
    min = lst[0][1]

    for k in range(1, n):
        if lst[k][1] < min:
            min = lst[k][1]
            cnt += 1

    print(cnt)
    lst = []