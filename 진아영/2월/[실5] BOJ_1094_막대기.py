def change(n, s):
    if n == 0:
        return s
    change(n // 2, s + str(n % 2))

print(change(23, ''))  # None 나오는데 return 써줬는데 왜 결과 안나오는거 ? ㅠㅠ

#------------------성공 수식-----------------------------------------
def change(n):
    global result
    if n == 0:
        return
    if n % 2 == 1:
        result += 1
    change(n // 2)

result = 0
change(int(input()))

print(result)
