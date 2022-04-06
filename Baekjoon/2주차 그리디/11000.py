import sys, heapq

n = int(sys.stdin.readline())
lst = []
heap = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    lst.append([a, b])
    
lst = sorted(lst, key = lambda x : x[0])
heapq.heappush(heap, lst[0][1])

for i in range(1, n):
    if lst[i][0] < heap[0]:
        heapq.heappush(heap, lst[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, lst[i][1])

print(len(heap))
