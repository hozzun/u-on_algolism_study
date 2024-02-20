# 메모리 110272 / 시간 128ms

N, K = list(map(int, input().split()))

arr_all = []
for i in range(N):
    arr = list(map(int, input().split()))
    arr_all.append(arr)

for i in arr_all:
    if i[0] == K:  # 알고싶은 국가의 메달 정보 저장.
        gold = i[1]
        sil = i[2]
        brz = i[3]
        arr_all.remove(i)
rank = N  # 초기 rank 마지막 등수로 설정

# 다른 국가와 금메달 수부터 비교하여 메달 수가 많다면 등수 up
for j in arr_all:
    if j[1] < gold:
        rank -= 1    
    elif j[1] == gold:
        if j[2] < sil:
            rank -= 1
        elif j[2] == sil:
            if j[3] <= brz:
                rank -= 1
print(rank)
