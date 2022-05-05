import sys

def bi_search(target, data):
    start = 0 
    end = data[-1]
    sum = 0
    result = -1

    while start <= end:
        sum = 0
        cen = (start + end) // 2
        for i in data:
            tmp = i - cen
            if tmp > 0:
                sum += tmp

        if sum >= target:
            result = cen
            start = cen + 1
        else:
            end = cen - 1
    return result

n, m = map(int, sys.stdin.readline().split())
lst = sorted(list(map(int, sys.stdin.readline().split())))

print(bi_search(m, lst))
