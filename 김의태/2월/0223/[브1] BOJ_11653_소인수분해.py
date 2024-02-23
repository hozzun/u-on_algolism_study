# python3 : 31120kb 1500ms, pypy : 109240kb 228ms
# idea : 나눠줄 수를 하나씩 더해주면서 소수 구하기, 합성수는 체크될 수가 없음.
n = int(input())

x = 2 # 소수는 2부터니까
answer = []
while n != 1:
    if n % x == 0:
        n = int(n / x)
        print(x)
    else:
        x += 1
