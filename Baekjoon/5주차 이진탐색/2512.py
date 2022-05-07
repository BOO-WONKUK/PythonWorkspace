import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

start = 0 
end = max(lst)
result = 0

while start <= end :
    sum = 0
    mid = (start + end) // 2
    for i in lst:
        if i > mid:
            sum += mid
        else:
            sum += i
    if sum <= m:
        result = mid
        start = mid + 1
    else:
        end  = mid - 1
print(result)