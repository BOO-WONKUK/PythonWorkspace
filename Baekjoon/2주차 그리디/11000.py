import sys

n = int(sys.stdin.readline())
lst = []
s, e = 0 , 0
cnt = 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    lst.append([a, b])
lst = sorted(lst)
check = [i for i in range(n)] 

for i in range(n):
    e = lst[i][1]
    for j in range(n):
        if i < j:
            s = lst[j][0]
            if e >= s:
                
