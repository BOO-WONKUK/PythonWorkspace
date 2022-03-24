a,b,c = map(int, input().split())
n = 0
if a == b == c:
    n = a * 1000 + 10000
elif a == b :
    n = a * 100 + 1000
elif b == c :
    n = b * 100 + 1000
elif a == c :
    n = a * 100 + 1000
else:
    n = max(a,b,c) * 100
print(n)