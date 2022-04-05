import sys, heapq

n = int(sys.stdin.readline())
lst = []


for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    lst.append([a, b])

lst = sorted(lst, key = lambda x : x[1])
p_list=[]
for i in lst:
  heapq.heappush(p_list, i[0])
  if (len(p_list)>i[1]):
    heapq.heappop(p_list)

print(sum(p_list))