import sys

n, m = map(int, sys.stdin.readline().split())
lst = []
result = [[i] for i in range(n + 1)]
for _ in range(m):
    lst.append(list(map(int, sys.stdin.readline().split())))

for j, k, l in lst:
    if j == 0:
        result[k] = result[k] + result[l]
        result[l] = result[k]
    elif j == 1 and k == l:
        print("yes")
    elif j == 1 :
        if (k in result[k] and l in result[k]) and (k in result[l] and l in result[l]):
            print("yes")
        else:
            print("no")
