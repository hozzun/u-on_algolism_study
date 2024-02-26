# 메모리 109240 / 시간 124ms

n = int(input())

arr = [[0]*100 for _ in range(100)]   # 0으로 채운 배열 생성
cnt = 0

for _ in range(n):
    p1, p2 = map(int, input().split())   # 색종이 왼쪽 아래 모서리 좌표

    for i in range(10):     # 색종이 위치에 1 할당
        for j in range(10):
            if arr[p2+i][p1+j] != 1:   # 겹치는 부분이 아니라면 count (cnt == 넓이)
                cnt += 1
            arr[p2+i][p1+j] = 1
print(cnt)
