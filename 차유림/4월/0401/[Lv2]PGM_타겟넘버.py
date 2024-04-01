# 프로그래머스 레벨2 타겟넘버

def dfs(i, op_val, numbers, target):
    global cnt
    
    if i == len(numbers): # 만약 i 가 len(numbers) = 5일때 
        if op_val == target: # 계산결과가 타겟이랑 같으면 
            cnt += 1 # +1 해줌 
        return 
    
    dfs(i + 1, op_val + numbers[i], numbers, target) # + 일때
    dfs(i + 1, op_val - numbers[i], numbers, target) # - 일때
    
def solution(numbers, target):
    global cnt
    dfs(0, 0, numbers, target)
    
    return cnt

cnt = 0 # 카운트 해줄 변수
