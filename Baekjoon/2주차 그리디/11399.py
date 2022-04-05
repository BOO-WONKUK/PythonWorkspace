import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
sum, time = 0, 0

for i in range(n):
    sum += lst[i]
    time += sum
print(time)