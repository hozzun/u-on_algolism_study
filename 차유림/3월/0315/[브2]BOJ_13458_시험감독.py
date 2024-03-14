# 백준 13458번 시험 감독 메모리 216480kb 시간 376ms 코드길이 320b
# 메모리 줄이고 싶어서 다른거로 냈더니 144340kb 시간 772ms 코길 268b 
N = int(input())
num = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = 0 # 시험 감독관 수 카운트 

for i in range(N):
    num[i] = num[i] - B # 총 감독관은 무조건 1명씩 필요하니까 num[i] = num[i] - B 로 바꿔주고 
    cnt += 1 # cnt +1 해줌 
    if num[i] > 0: # 그런데 만약에 바꿔준 값이 0보다 크다면 부감독관이 필요하다는 말임! 0보다 작을 떈 상관 x
        cnt += num[i] // C # num[i]를 C만큼 나눈 몫을 더해줌 ( 딱 나누어 떨어지거나 나머지가 생길 때 )
        if num[i] % C != 0: # 만약 나머지가 0이 아니라면 
            cnt += 1 # cnt += 1 해줌 ( C보다 작을 때인 경우도 포함됨 )

print(cnt)
