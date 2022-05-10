import sys

t = int(sys.stdin.readline())

for _ in range(t):
    dp = [0] * 101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    dp[6] = 3
    dp[7] = 4
    dp[8] = 5
    n = int(sys.stdin.readline())
    for i in range(9, n + 1):
        dp[i] = dp[i - 1] + dp[i - 5]
    print(dp[n])