import sys, heapq

n = int(sys.stdin.readline())
h = []

for _ in range(n):
    a = int(sys.stdin.readline())

    if a != 0:
        heapq.heappush(h, -a)
    else:
        if len(h) == 0:
            print("0")
            continue
        print(-heapq.heappop(h))
