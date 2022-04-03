import sys, copy

n = int(sys.stdin.readline())
a = list(sys.stdin.readline().rstrip())
b = list(sys.stdin.readline().rstrip())
lst = copy.deepcopy(a)
result = []

for j in a, lst:
    cnt = 0
    if j == a:
        if j[0] == '0':
            j[0] = '1'
            j[1] = '1'
        elif j[0] == '1':
            j[0] = '0'
            j[1] = '0'
        cnt += 1
    for i in range(1,n):
        if i != n - 1:
            if j[i - 1] != b[i - 1]:
                if j[i] == '0':
                    j[i] = '1'
                elif j[i] == '1':
                    j[i] = '0'
                if j[i - 1] == '0':
                    j[i - 1] = '1'
                elif j[i - 1] == '1':
                    j[i - 1] = '0'
                if j[i + 1] == '1':
                    j[i + 1] = '0'
                elif j[i + 1] == '0':
                    j[i + 1] = '1'
                cnt += 1

        elif i == n - 1:
            if j[i - 1] != b[i - 1]:
                if j[i] == '1':
                    j[i] = '0'
                elif j[i] == '0':                        j[i] = '1'
                if j[i - 1] == '0':
                    j[i - 1] = '1'
                elif j[i - 1] == '1':
                    j[i - 1] = '0'
                cnt += 1
            # for k in range(n):
            #     if j[k] == b[k]:
            #         if k == n - 1:
            if j == b:
                result.append(cnt)

# if (a != b and lst != b) or :
if len(result) == 0:
    print(-1)
elif len(result) != 0:
    print(min(result))
