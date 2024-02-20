# 테케 두개는 순위랑 정답 둘다 맞는데 채점은 틀렸다하고 원인을 못찾겠음.. 개열받아서 못해먹겠삼 포기!!!!!!

N, K = list(map(int, input().split()))
arr = [0] * (N+1)
grade = [0] * (N+1)

for _ in range(N):
    contry, g, s, b = list(map(int, input().split()))
    arr[contry] = [g, s, b]

for i in range(1, 4):   # i = 금,은,동 번호
    max_medal = []
    max_medal_num = 0
    
    # 메달 수 비교하여 순위 매기기
    for j in range(1, N+1):  # j : 국가번호
        if max_medal_num < arr[j][i-1]:
            max_medal = [j]       # 메달 가장 높은 국가번호 재설정
            max_medal_num = arr[j][i-1]     # 그때의 메달 수 재설정
        elif max_medal_num == arr[j][i-1]:
            max_medal.append(j)   # 메달 수가 같으면 리스트에 국가번호 append

    while max_medal:
        # 하나씩 뽑아서 등수(i) 표시
        a = max_medal.pop()
        grade[a] = i
        # 이미 순위 매겨진 국가는 다음 메달 순위 매길때 영향 안받도록 0으로 설정
        arr[a] = [0, 0, 0]

print(grade[K])
