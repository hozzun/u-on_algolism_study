# 10773번 제로 메모리 31900KB 시간 3976 ms
def push(item):
    global top
    top += 1
    stack[top] = item
def pop():
    global top
    stack[top] = 0
    top -= 1

K = int(input())
stack = [0] * K
sum_stack = 0
top = -1
for i in range(K):
    num = int(input())
    if num != 0:
        push(num)
    else:
        pop()

for st in stack:
    sum_stack += st

print(sum_stack)
