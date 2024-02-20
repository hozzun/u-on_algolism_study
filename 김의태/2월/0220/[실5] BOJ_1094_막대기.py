# 31120kb 40ms
x = int(input())
stack = [64] # 스택을 이용, 초기값

while sum(stack) > x:   #문제 그대로 조건 진행

    bar = stack.pop() #꺼내서 반 가르고 버릴지 말지 선택하는 과정
    bar = bar / 2
    stack.append(bar)
    if x > sum(stack):
        stack.append(bar)

print(len(stack)) # 몇개의 막대기로 x와 같아지는지 출력!
