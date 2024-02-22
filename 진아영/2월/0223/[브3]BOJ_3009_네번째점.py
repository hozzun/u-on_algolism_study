r = [] # x좌표
c = [] # y좌표

for _ in range(3):
    a, b = list(map(int, input().split()))
    if a in r:        # 이미 있으면
        r.remove(a)   # 짝이 맞으니까 비워줌
    else:
        r.append(a)
    if b in c:
        c.remove(b)
    else:
        c.append(b)

print(r[0], c[0])   # 남은 (필요한) 짝 출력
