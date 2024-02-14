mushs = [int(input()) for _ in range(10)] #입력값

scores = 0 #버섯총합
adj_100 = 101 # 100에서 가장 가까운 최소값을 구하기 위한 초기변수설정
for mush in mushs:
    scores += mush
    if adj_100 >= abs(100 - scores):
        adj_100 = abs(100 - scores) # 버섯 총합이 100과의 거리가 가까울수록 저장
        answer = scores # adj_100이 새로 할당될때 점수 할당

print(answer) #출력.
