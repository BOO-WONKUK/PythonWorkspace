import sys, math

n = int(sys.stdin.readline())
lst = []
money = 0
pre1, pre0 = math.inf, 0
cnt = 0
high = 0
pre = []
tmp = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    lst.append([a, b])

lst = sorted(lst, key = lambda x : (-x[1], -x[0]))
# print(lst)
for i in range(n):
    if i == 0:
            high = lst[i][1]
    if pre1 > lst[i][1]:
        pre1 = lst[i][1]
        pre0 = lst[i][0]
        if len(pre) == 0 or (min(pre) < lst[i][0]) :
            pre.append(lst[i][0])
        # if lst[i][0] > min(pre):
        #     # money -= min(pre)
        #     pre.remove(min(pre))
        # money += lst[i][0]
    elif pre1 == lst[i][1]:
        if pre0 < lst[i][0]:
            pre.append(lst[i][0])  
            pre.remove(min(pre))  
        elif pre0 == lst[i][0]:
            pre.append(lst[i][0])    
        
    if len(pre) > high:
        # if lst[i][0] > min(pre):
            # money -= min(pre)
            pre.remove(min(pre))
        

            # money += max(pre)

# # print(lst)
# for i in range(n):
#     if cnt2 > lst[n - 1][1] + 1:
#         break
#     if cnt1 != lst[i][1]:
#         money1 += lst[i][0]
#         cnt1 += 1

#     if cnt2 != lst[i][1]:
#         pre.append(lst[i][0])
#         money2 += lst[i][0]
#         cnt2 += 1

#     elif cnt2 == lst[i][1]:
#         if lst[i][0] >= min(pre):
#             money2 -= min(pre)
#             if lst[i][0] != min(pre):
#                 pre.remove(min(pre))
#             money2 += lst[i][0]
#             cnt2 += 1
#             continue
    
# print(max(money1, money2))
print(sum(pre))