import sys

def reverse(x):
    if x == '1':
        return '0'
    elif x == '0':
        return '1'

n, m = map(int, sys.stdin.readline().split())
lst = []
ans = []
cnt = 0

for _ in range(n):
    lst.append(list(sys.stdin.readline()))

for _ in range(n):
    ans.append(list(sys.stdin.readline()))

for i in range(1, n - 1):
    for j in range(1, m - 1):
        if lst[i - 1][j - 1] != ans[i - 1][j - 1]:
            for k in range(3):
                for l in range(3):
                    lst[i - 1 + k][j - 1 + l] = reverse(lst[i - 1 + k][j - 1 + l])
            cnt += 1
        else:
            continue

if lst == ans:
    print(cnt)
else:
    print('-1')
