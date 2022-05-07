import sys

n,h = map(int,sys.stdin.readline().split(" "))
side_even = [0] * h
side_odd = [0] * h
for i in range(0,n):
    k = int(sys.stdin.readline())
    if i % 2 == 0:
        side_even[k-1] += 1
    else:
        side_odd[k-1] += 1
for i in range(h-1,0,-1):
    side_odd[i-1] += side_odd[i]
    side_even[i-1] += side_even[i]

minn = 200001
ans = 0

for i in range(0,h):
    t = side_even[i] + side_odd[h - 1 - i]
    if t < minn:
        minn = t
        ans = 0
    if t == minn:
        ans += 1
print(minn , end=" ")
print(ans)