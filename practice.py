import sys

N=int(sys.stdin.readline())
lst = []
count=1

for i in range(N):
    lst.append(list(map(int,sys.stdin.readline().split())))
lst.sort()
lst = sorted(lst, key=lambda x:x[1]) 
    
tmp = lst[0][1]

for k in range(N):
    try:
        if tmp <= lst[k+1][0]:
            tmp = lst[k+1][1]
            count+=1
        else:
            pass
    except IndexError:
        break

print(count)