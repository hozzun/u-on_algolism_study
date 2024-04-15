# 소수 찾기 
# 100점 인데... 테스트 10 번이 채점하는데 굉장히 오래걸림... 
# 3023.98ms 걸렸다는데 .. 흠냐링 .. 뭔가 더 시간이 짧은 코드가 있을 듯? 

from itertools import permutations
def solution(numbers):
    answer = 0
    digit = []
    for i in numbers: # digit에 numbers 한자리씩 쪼개서 넣어줌 
        digit.append(i)

    digit_lst = []
    for i in range(1, len(numbers) + 1): 
        # 1 부터 numbers 의 길이만큼,,  ex. 1자리수 모든 순열, 2자리 수 모든 순열 구하기
        digit_lst += list(permutations(digit, i))
        
    for j in range(len(digit_lst)): # 조인해서 합쳐줌 ! 
        digit_lst[j] = int("".join(digit_lst[j]))

    digit_lst = set(digit_lst) # digit_lst 는 set으로 중복을 없애준다 
     
    for num in digit_lst: # 리스트를 돌면서 
        if prime(num) == True: # 만약에 소수이면 
            answer += 1 # += 1

    return answer 

def prime(num):
    if num < 2: # number 가 2보다 작으면 소수 아니니까 무조건 false 
        return False
    for i in range(2, num): # 2부터 num-1 까지 전부 나누는데 
        if num % i == 0: # 하나라도 나머지가 0 이라면 false 임
            return False
    return True # 다 통과하면 true~~ 


