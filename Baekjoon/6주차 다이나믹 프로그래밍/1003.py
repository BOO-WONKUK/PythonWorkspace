dic = {1:1, 2:1}

def fib_memoization(n):
    if n in dic:
        return dic[n]
    
    dic[n] = fib_memoization(n-1) + fib_memoization(n-2)
    return dic[n]

N = int(input())

for i in range(N):
    a = int(input())
    if a == 0:
        print("{0} {1}".format(1, 0))
    elif a == 1:
        print("{0} {1}".format(0, 1))
    else:
        print("{0} {1}".format(fib_memoization(a - 1) ,fib_memoization(a)))