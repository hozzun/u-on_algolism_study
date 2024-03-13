# 파이썬 144340 Kb, 732 ms, 397 B

N = int(input())  # 시험장 수
test = list(map(int, input().split()))
B, C = map(int, input().split())         # 총, 부감독관이 감시할 수 있는 응시자 수

test = list(map(lambda x: x-B, test))    # 총 감독관이 관리할 수 있는 학생 뺴주기 = 부감독이 관리해야할 학생 수
teacher = N                              # 필요한 총 감독수 = 시험장 수

for i in range(N):
    if test[i] > 0:   # 부감독관이 필요한 경우
        t = test[i]   # 남은 학생들
        teacher += t // C   # 몫을 필요한 부감독 수로 저장
        if t % C:           # 나머지가 있으면
            teacher += 1    # 부감독 1명 추가

print(teacher)
