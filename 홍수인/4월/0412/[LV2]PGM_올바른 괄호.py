def solution(s):
    answer = True
    stack = []
    
    for i in s:        # input 문자열s 순회
        if i == '(':   # 여는 괄호면 stack에 넣기
            stack.append(i)
        else:          # 닫는 괄호일 경우
            if len(stack) == 0:    # stack에 짝 없으면 return False
                return False
            elif stack[-1] == '(':   # stack에 짝 있으면 여는 괄호 pop
                stack.pop()
                
    if len(stack) != 0:   # 반복문 종료 후 stack에 남은 요소가 있으면 return False
        return False
        
    return answer       # 위의 조건에 모두 성립하지 않으면 (True인 경우) return True
