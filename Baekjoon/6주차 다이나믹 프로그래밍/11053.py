import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
dp = [1] * 1001

for i in range(1, n):
    for j in range(0, i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))