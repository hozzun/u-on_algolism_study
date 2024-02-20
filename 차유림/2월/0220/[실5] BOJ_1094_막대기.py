# 백준 1094번 막대기 메모리 31120 KB 시간 44ms

# 처음에 return 안써서 안나옴 ㅋㅋㅋㅋ 바보 ㅜㅜ 
# idea x를 이진수로 변환해서 1인 부분만 카운트 해주기 

X = int(input())
cnt = 0
def two(n):
    global cnt 
    if n % 2 == 1: # n을 2로 나누었는데 나머지가 1이면 
        cnt += 1 # 카운트 추가 
        return two(n // 2) # 몫만 다시 재귀로 해준다
    elif n != 0: # n을 2로 나누었는데 나머지가 1이 아닌데 n이 0이 아닐 때 
        return two(n // 2) # 몫만 다시 재귀로 고고
    else: 
        return cnt # 끝났을 때 cnt 반환 

result = two(X)
print(result)
