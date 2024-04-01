# 100점

def dfs(numbers, target, idx, total):
    global answer # 글로벌로 받기
    
    if idx == len(numbers) and total == target: # 끝까지 다 돌아보았고, 합이 target이랑 같으면 1 증가 후 리턴
        answer += 1
        return
    
    elif idx == len(numbers): # 그냥 끝까지만 다 돌았으면 리턴
        return
    
    dfs(numbers, target, idx + 1, total + numbers[idx]) # 덧셈
    dfs(numbers, target, idx + 1, total - numbers[idx]) # 뺄셈

    
def solution(numbers, target):
    global answer # answer 글로벌로 내보내기
    answer = 0
    
    dfs(numbers, target, 0, 0)
    
    return answer
