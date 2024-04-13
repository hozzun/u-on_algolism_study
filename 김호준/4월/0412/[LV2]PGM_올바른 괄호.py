# 100점
# 그냥 리스트로 하니까 효율성테스트 시간초과나서 덱으로 바꿔서 푸니까 맞음
# 소프티어 1번문제처럼 풀었삼

from collections import deque

def solution(s):
    answer = True
    
    stack = deque()
    for i in s:
        if i == '(': # 여는 괄호 일땐 그냥 집어넣음
            stack.append(i)
        elif i == ')': # 닫는 괄호일때
            if not stack: # 비어있으면
                stack.append(i) # 집어넣고
            elif stack[0] == '(': # 여는 괄호가 있으면 pop해줌
                stack.popleft()
    
    if not stack: # 짝이 다맞아서 비어있으면 True
        answer = True
    else: # 아니면 False
        answer = False
    
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer
