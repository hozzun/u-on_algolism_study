# 메모리 : 144340, 시간 : 600ms, 코드 길이 : 305B
n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

result = n   # 총감독관 1명
for i in a:
    num = i-b
    if num > 0:
        if num % c == 0:
            result += num//c
        else:
            result += (num//c + 1)
    else:
        continue
print(result)
