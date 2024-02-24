# 백준 11653번 소인수분해 메모리 109240kb 시간 228ms

N = int(input())
num = []
i = 2
while N > 1: # 소인수분해는 N 이 1이 될때까지 하므로 범위를 이렇게 설정해줌 
    if N % i == 0:
        num.append(i)
        N = N // i
    else:
        i = i + 1

for i in num:
    print(i)

# -----------------------------------------------------------------
# 시간초과 남 ㅠㅠ 
N = int(input())
num = []
i = 2
while N > 0: # N이 0보다 클 때 까지
    if N % i == 0: # 2로 나눠서 나머지가 0 이면
        num.append(i) # num 리스트에 추가
        N = N // i # N 은 N을 i 로 나눈 몫으로 바꿔줌
        if N == 1: # N이 1이 된다면 소인수분해 끝난것이므로
            break # 멈춘다
    else: # N이 2로 안나뉜다면
        i = i + 1 # i+1 해서 반복

for i in num:
    print(i)
