MAX = 1000000


n = int(input())
ans = []

dp = [1] * (MAX+1)
s = [0] * (MAX+1)

for i in range(2,MAX+1):
    j = 1
    while i*j <= MAX:
        dp[i*j] += i
        j+=1

for i in range(1,MAX+1):
    s[i] = s[i-1] + dp[i]

for _ in range(n):
    tmp = int(input())
    ans.append(s[tmp])
    
print('\n'.join(map(str,ans)))