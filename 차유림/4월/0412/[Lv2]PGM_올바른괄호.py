# 올바른 괄호 
# 정확성 69.5 효율성 30.5 
def solution(s):
    stack = [] 
    result = True

    for i in s: # s를 돌면서 
        if i == '(': # ( 괄호일때
            stack.append(i) # 스택에 넣어줌
        elif i == ')': # ) 일때
            if stack and stack[-1] == '(': # 스택에 값이 존재하고 가장 바깥쪽에 있는게 (일때
                stack.pop() # 팝해줌
            else: # 그게 아니면
                result = False # false 반환
                return result
            
    if stack: # 다 돌았는데도 값이 존재하면 
        result = False # false 반환 
        return result
    
    return result 
