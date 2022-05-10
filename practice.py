n = int(input())
lst = list(map(int, input().split()))
max = max(lst)
print("{:0.3f}".format((sum(lst) / max) * 100 / n))