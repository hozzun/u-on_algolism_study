import sys
sys.setrecursionlimit(10000000)

def dfs(i, cur, arr, tar):  # idx, 연산, 숫자 배열, 타겟
    global answer
    
    if i == len(arr):
        if cur == tar:
            answer += 1
        return
    
    # 더하기 했을 경우
    dfs(i+1, cur + arr[i], arr, tar)
    
    # 빼기 했을 경우
    dfs(i+1, cur - arr[i], arr, tar)
    
    

def solution(numbers, target):
    global answer   # 이거 어케하는지 몰라서 호준오빠 코드 훔쳐봄 히히
    
    answer = 0
    
    dfs(0, 0, numbers, target)
    
    return answer
