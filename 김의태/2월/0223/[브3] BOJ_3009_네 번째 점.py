# 31120kb 40ms
# idea : x좌표와 y좌표의 숫자의 종류는 각각 2개씩일 수밖에 없다! 왕따인걸 찾자!
location = [list(map(int, input().split())) for _ in range(3)]

x = [] # x좌표만
y = [] # y좌표만

for i in location:
    x.append(i[0])
    y.append(i[1])

answer = []

# 왕따인 거 찾기
for n in x:
    if x.count(n) == 1:
        answer.append(n)

for n in y:
    if y.count(n) == 1:
        answer.append(n)

print(*answer)
