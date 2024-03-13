# 파이파이 146384 KB, 2936 ms, 677 B
# 파이썬 시간초과

N = int(input())
num_list = []

for _ in range(N):
    num_list.append(int(input()))

num_list.sort()

print(round(sum(num_list) / N))     # 1. 산술평균
print(num_list[N//2])               # 2. 중앙값


# 3. 최빈값

num_list_count = []
for i in list(set(num_list)):
    a = num_list.count(i)
    num_list_count.append((a, i))  # 숫자 i의 count 수 a, 두개 묶어서 튜플로 저장

num_list_count.sort(reverse=True)  # 큰수부터 정렬 (count 큰수로 정렬)
max_count = num_list_count[0][0]   # 최빈 count 저장 (num_list_count의 제일 앞 값)
max_count_list = []                # 최빈 숫자를 저장할 리스트

for j in num_list_count:
    if j[0] == max_count:
        max_count_list.append(j)

if len(max_count_list) > 1:         # 최빈값이 여러개일 경우
    print(max_count_list[-2][1])
else:
    print(max_count_list[0][1])



print(num_list[-1] - num_list[0]) # 4. 범위


