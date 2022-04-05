import sys

n = int(sys.stdin.readline())

lst = []

def fun(x, y):
    if x == "push":
        lst.append(y)
    elif x == "pop":
        if len(lst) == 0:
            print("-1") 
        else:
            print(lst.pop(-1))
    elif x == "size":
        print(len(lst))
    elif x == "empty":
        if len(lst) == 0:
            print("1")
        else:
            print("0")
    elif x == "top":
        if len(lst) == 0:
            print("-1")
        else:
            print(lst[-1])
    


for _ in range(n):
    command = sys.stdin.readline()
    if "push" in command:
        a, b= command.split()
        fun("push",b)
    elif "pop" in command:
        fun("pop",0)
    elif "size" in command:
        fun("size",0)
    elif "empty" in command:
        fun("empty",0)
    elif "top" in command:
        fun("top", 0)
