# 31120kb 40ms
# idea : 문제의 조건이 많은 경우 그 조건을 그대로 코딩으로 옮기기. 이 문제는 실제 막대기를 자른다고 생각.(스택으로 구현)
x = int(input())
stack = [64] # 스택을 이용, 초기값

while sum(stack) > x:   #문제 그대로 조건 진행

    bar = stack.pop() #꺼내서 반 가르고 버릴지 말지 선택하는 과정
    bar = bar / 2
    stack.append(bar)
    if x > sum(stack):
        stack.append(bar)

print(len(stack)) # 몇개의 막대기로 x와 같아지는지 출력!
