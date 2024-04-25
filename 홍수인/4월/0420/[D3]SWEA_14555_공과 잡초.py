T = int(input())
for tc in range(1, T+1):
    ball = input()
    stack = []
    cnt = 0
    for i in ball:
        if i == '|':   # 잡초인데 스택이 비어있지 않고, 스택의 마지막이 (이면 pop하고 cnt+1
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                    cnt += 1
            else:
                stack.append(i)   # 스택이 비어있지 않고, 마지막 요소가 (이 아니면 append
        elif i == '(':     # 공의 왼쪽 부분이면 append
            stack.append(i)
        elif i == ')':      # 공의 오른쪽 부분인 경우, stack의 마지막 요소가 잡초 or (라면 cnt + 1 
            if stack:
                if stack[-1] == '|' or stack[-1] == '(':
                    stack.pop()
                    cnt += 1
    print(f'#{tc}', cnt)
