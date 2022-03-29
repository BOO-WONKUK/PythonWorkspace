from inspect import stack
from opcode import stack_effect
import sys

n = int(sys.stdin.readline())
stack = []
lst = []
cnt = 0
tmp = True

for _ in range(n):
    x = int(sys.stdin.readline())

    while cnt < x:
        cnt += 1
        stack.append(cnt)
        lst.append("+")

    if stack[-1] == x:
        stack.pop()
        lst.append("-")
    
    else:
        tmp = False
        print("NO")
        break
if tmp == True:
    for i in lst:
        print("{}".format(i))