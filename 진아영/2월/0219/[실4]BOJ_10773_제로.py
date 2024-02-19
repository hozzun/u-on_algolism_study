stack = []

for i in range(int(input())):
    a = int(input())
    if not a:
        stack.pop()
    else:
        stack.append(a)

print(sum(stack))
