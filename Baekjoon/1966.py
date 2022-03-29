import sys

n = int(sys.stdin.readline())

for _ in range(n):
    h = []
    x, y = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    lstsub = [False for i in range(x)]
    lstsub[y] = True
    cnt = 0

    while True:
        if lst[0] == max(lst):
            cnt += 1
            if lstsub[0] == True:
                print(cnt)
                break
            else:
                del lst[0]
                del lstsub[0]
        else:
            lst.append(lst[0])
            lstsub.append(lstsub[0])
            del lst[0]
            del lstsub[0]