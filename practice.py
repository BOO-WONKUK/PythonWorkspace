import sys

t = int(sys.stdin.readline())

lst = [True] * (10001)
lst[0], lst[1] = False, False
for i in range(2, 101):
    if lst[i]:
        for j in range(2*i, 10001, i):
            lst[j] = False

for _ in range(t):
    n = int(sys.stdin.readline())
    lstsub = lst[:n + 1]
    check = []
    minus = []
    a = 0

    while a <= int(n/2):
            if lstsub[a] == True and lstsub[n - a] == True:
                check.append(a)
                check.append(n - a)
                minus.append(n - 2 * a)
                lstsub[a] = False
                a += 1
            else:
                lstsub[a] = False
                a += 1

    print(check[minus.index(min(minus)) * 2],check[minus.index(min(minus)) * 2 + 1]) 
    