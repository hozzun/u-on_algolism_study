# 백준 2851번 슈퍼마리오 
score = []
scores = 0
for i in range(10):
    num = int(input())
    score.append(num) # score리스트를 만들어서 점수들 저장함 

for i in score: # score의 i를 순회
    p_scores = scores # p_scores에 scores 저장 현재 -1 값 저장 이전 합을 구한 것 
    scores += i # score에 i값 누적해서 더함 
    if scores >= 100: # 만약 현재 합이 100 이상이라면 
        if abs(100 - scores) > abs(100 - p_scores): # 절댓값 비교해서 절댓값이 작은 쪽을 출력 
            # ex 98, 103 이라면 103-100 > 100-98 임 98 을 출력해야 하므로 scores에 p_scores를 저장해야함 
            scores = p_scores # scores에 p_scores 값을 저장 
        break

print(scores)
