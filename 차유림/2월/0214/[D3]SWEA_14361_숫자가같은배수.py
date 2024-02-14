# swea 14361 숫자가 같은 배수 
def f(i, k):
    global result
    if i == k: # i가 k, N의 길이와 같아지면 
        new_num = int(''.join(P)) # new_num에 조인 , ['1','4','7'...] 으로 나오는 걸 147...로 할당해줌 
        if new_num % int(N) == 0 and new_num > int(N): # 새로운 수가 N으로 나누어 져야 하고 N보다 크다면 
             result = 'possible' # 가능하다고 출력 
    else:
        for j in range(i, k): # 순열 구하는 코드 
            P[i], P[j] = P[j], P[i]
            f(i + 1, k)
            P[i], P[j] = P[j], P[i]

T = int(input())
for tc in range(1, T+1):
    N = input()
    P = [i for i in N] # P에 N 하나하나씩 넣은 리스트 만들어준다 
    result = 'impossible'
    f(0, len(N))
    print(f"#{tc} {result}")
