import sys, heapq

n = int(sys.stdin.readline())
h = []


for _ in range(n):
    a = int(sys.stdin.readline())

    if a != 0:
        if a < 0:
            heapq.heappush(h, (-a, a))
        elif a > 0:
            heapq.heappush(h, (a, a))
        
    else:
        if len(h) == 0:
            print("0")
            continue
        print(heapq.heappop(h)[1])
        
