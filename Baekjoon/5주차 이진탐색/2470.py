import sys

n = int(sys.stdin.readline())
lst = sorted(list(map(int, sys.stdin.readline().split())))
sublst = []


for i in lst:
    start = 0
    end = max(lst)
    result = 0
    min = 1000000000

    while start <= end:
        mid = (start + end) // 2

        if i + mid <= min:
            sublst.append([i, mid, min])
            start = mid + 1
        else:
            end  = mid - 1
a = [j[1] for j in sublst]
b = min(a)
idx = a.index(b)
print(sublst[idx][0], sublst[idx][1])

