import sys 

n, k = map(int, sys.stdin.readline().split())
lst = []

for _ in range(n):
    x = int(sys.stdin.readline())
    lst.append(x)
tmp = -1
cnt = 0
while True:   
    cnt += k // lst[tmp]
    k %= lst[tmp] 
    tmp -= 1
    if k == 0:
        break
print(cnt)