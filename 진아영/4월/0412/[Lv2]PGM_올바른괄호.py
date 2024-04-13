def solution(s):
    answer = True
    stack = 0
    for char in s:
        if char == '(':           # 여는괄호일때
            stack += 1            # 스택 += 1
        else:                     # 닫는괄호일때
            if stack:             # 쌓인 스택 있으면 (남는 여는괄호 있으면)
                stack -= 1        # 스택 -= 1 (여는괄호 하나 사용)
            else:                 # 닫는괄호일때 남는 여는괄호 없으면
                answer = False    # 결과 바꾸고
                break             # 브레이크
    if stack:               # for문 다 돌았는데도 여는괄호 남았으면
        answer = False      # 결과 바꿈

    return answer
