import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    lst.sort(reverse=True)
    ans = [0 for _ in range(n)]
    tmp = 0
    result = 0

    if n % 2 == 1:
        start = n//2
    elif n % 2 == 0:
        start  = n//2 -1

    for i in range(n):
        if i % 2 == 1:
            tmp = 1
            a = 1
        else:
            tmp = -1
            a = 0
        if i == 0:
            ans[start] = lst[i]
        else:
            ans[start + tmp * (i//2 + a)] = lst[i]

    for j in range(n - 1):
        if result < (abs(ans[j + 1] - ans[j])):
            result = abs(ans[j + 1] - ans[j])
        if j == n - 2:
            if result < (abs(ans[0] - ans[n - 1])):
               result = abs(ans[0] - ans[n - 1])
    print(result)