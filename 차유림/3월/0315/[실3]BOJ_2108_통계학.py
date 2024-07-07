# # 백준 2108번 통계학 
# 최빈값 어캐 구함???????? 이상해 ㅜ ㅜ 시간초과나고 난리났스

N = int(input()) # N은 홀수임
num_lst = []
for i in range(N):
    num = int(input())
    num_lst.append(num)

num_lst.sort()
average = round(sum(num_lst) / N)
print(average)

middle = num_lst[N // 2]
print(middle)

from collections import Counter # 빈도수를 체크해주는 counter 함수... 이런게 있도라.. 
counts = Counter(num_lst)
most_common = counts.most_common() # num, bin 튜플 형태로 내림차순 해서 출력됨
max_bin = most_common[0][1]

arr = []
for num, bin in most_common:
    if bin == max_bin:
        arr.append(num)

if len(arr) > 1:
    print(arr[1])
else:
    print(arr[0])

num_range = max(num_lst) - min(num_lst)
print(num_range)


# N = int(input()) # N은 홀수임
# num_lst = []
# for i in range(N):
#     num = int(input())
#     num_lst.append(num)

# num_lst.sort()
# average = round(sum(num_lst) / N)
# print(average)

# middle = num_lst[N // 2]
# print(middle)

# counts = [] * (N + 1)
# for i in num_lst:
#     a = num_lst.count(i)
#     counts.append(a)

# print(counts)

# max_val = max(counts)
# cnt = 0
# for i in range(1, N):
#     if counts[i] == max_val:
#         if counts[i] != counts[i-1]:
#             cnt += 1
#             if cnt == 2:
#                 print(num_lst[i])
#                 break
        

# num_range = max(num_lst) - min(num_lst)
# print(num_range)
