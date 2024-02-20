# 31120kb 100ms 100점 나옴(처음임 ㄷㄷ)
n, k = map(int, input().split())

rank = 1 # 최소 1등이므로 1 할당
score = [] # 메달개수 받을 리스트 생성

for i in range(n):
    score.append(list(map(int, input().split())))

score.sort(key=lambda x: x[0]) #알고싶은 k가 socre리스트의 2차원으로 묶여있음.
                               #근데 k를 기준으로 정렬시켜 인덱스로 퉁치면 2차원으로 k를 찾을 필요 없다고 생각함.

for i in range(n): # score리스트 다 돌기
    if score[i][1] > score[k-1][1]: #금메달이 많은 경우
        rank += 1
    elif score[i][1] == score[k-1][1] and score[i][2] > score[k-1][2]: #금은 같. 은이 많은 경우
        rank += 1
    elif score[i][1] == score[k-1][1] and score[i][2] == score[k-1][2] and score[i][3] > score[k-1][3]: #금,은 같. 동이 많은 경우
        rank += 1

print(rank)
