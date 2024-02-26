# 메모리 31120 KB, 시간 44 ms

paper = [[0] * 100 for _ in range(100)]

for _ in range(int(input())):
    r, c = list(map(int, input().split()))
    # 색칠하기랑 똑같이 색종이 붙이기
    for i in range(r, r+10):
        for j in range(c, c+10):
            paper[i][j] = 1

result = 0
# 색종이 붙은 부분 세기
for a in range(100):
    for b in range(100):
        if paper[a][b] == 1:
            result += 1

print(result)
