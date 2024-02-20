# 메모리 31120 시간 40ms

#----------------함수 만들기 실패작---------------------------------------------

def change(n, s):
    if n == 0:
        return s
    change(n // 2, s + str(n % 2))

print(change(23, '')) 
# None 나오는데 return 써줬는데 왜 결과 안나오는거 ? ㅠㅠ 재귀함수 이용해서 바로바로 이진법 만들고 1의 개수를 세고 싶었는데 실패함


#------------------성공 수식----------------------------------------------------


# 그림 그려보니까 이진법으로 구할 수 있을거 같아서 이진법으로 바꾸면서 1의 개수를 체크해줌

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
