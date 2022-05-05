import sys

k, n = map(int, sys.stdin.readline().split())
lst = []
for _ in range(k):
    lst.append(int(sys.stdin.readline()))
sum = sum(lst)
start = 1
end = sum // 2
result = 1

while start <= end and start >= 1:
    cnt = 0
    mid = (start + end) // 2
    for i in lst:
        cnt += i // mid
    if cnt < n:
        end = mid -1
    else:
        result = mid
        start = mid + 1
print(result)