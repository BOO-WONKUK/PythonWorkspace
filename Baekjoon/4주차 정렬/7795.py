import sys

t = int(sys.stdin.readline())

def bi_search(target, data):
    start = 0
    end = len(data) - 1
    result = -1

    while start <= end:
        mid = (start + end) // 2
        if data[mid] < target:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    lsta = sorted(list(map(int, sys.stdin.readline().split())))
    lstb = sorted(list(map(int, sys.stdin.readline().split())))
    cnt = 0    

    for i in lsta:
        cnt += bi_search(i, lstb) + 1

    print(cnt)