import sys

n = int(sys.stdin.readline())
lst  = sorted(list(map(int, sys.stdin.readline().split())))
sum = 0
tmp = 0
res = 0
result = []

cen = lst[(n - 1) // 2]

while True:
    tmp, tmpl, tmpr = 0, 0, 0
    cenl = cen - 1
    cenr = cen + 1
    for j in lst:
        tmp += abs(cen - j)
        tmpl += abs(cenl - j)
        tmpr += abs(cenr - j)
    
    if min(tmp, tmpl, tmpr) == tmpl:
        cen -= 1
        continue
    elif min(tmp, tmpl, tmpr) == tmp:
        result.append(cen)
        break
    else:
        cen += 1
        continue

print(min(result))

