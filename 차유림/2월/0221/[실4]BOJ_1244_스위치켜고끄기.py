# 백준 1244번 스위치 켜고 끄기 못하겠어 ㅜ ㅜ ㅜ ㅜ ㅜ ㅜ ㅜ ㅜ ㅜ ㅜ ㅜ ㅜ ㅜ ㅜ ㅜ ㅜ ㅜ
N = int(input())
switch = list(map(int, input().split()))
student_num = int(input())
for i in range(student_num):
    s , num = list(map(int, input().split()))
    
    if s == 1: # 남학생일 때 and  배수인거 어캐하지..?? - > 아영언니가 힌트줌 ㅎㅎ 
        for i in range(1, N + 1):
            if i % num == 0: # 스위치 번호 % 받은 번호 == 0 일 때 스위치 바꿔줌 
                if switch[i - 1] == 0 :
                    switch[i - 1] = 1
                else:
                    switch[i - 1] = 0

    if s == 2: # 여학생일 경우
        cnt = 1
        for j in range((N - num) // 2) :
            if switch[num-j-1] == switch[num+j-1]:
                cnt += 2
            elif switch[num-j-1] != switch[num+j-1]:
                    break
        # if cnt == 1:
        #     if switch[num-1] == 0:
        #         switch = 1
        #     else:
        #         switch[num-1] = 0
        if cnt != 1:
            for i in range(num - cnt//2 , num + cnt//2 + 1):
                if switch[i-1] == 0:
                    switch[i-1] = 1
                else:
                    switch[i-1] = 0


for i in range(0, N, 20):
    print(*switch[i : i+20])


# ------------------------------------------------------------------------
# 맞았다! 
# 백준 1244번 스위치 켜고 끄기 

N = int(input())
switch = list(map(int, input().split()))
student_num = int(input())
for i in range(student_num):
    s , num = list(map(int, input().split()))
    
    if s == 1: # 남학생일 때 and  배수인거 어캐하지..?? - > 아영언니가 힌트줌 ㅎㅎ 
        for i in range(1, N + 1):
            if i % num == 0: # 스위치 번호 % 받은 번호 == 0 일 때 스위치 바꿔줌 
                if switch[i - 1] == 0 :
                    switch[i - 1] = 1
                else:
                    switch[i - 1] = 0

    if s == 2: # 여학생일 경우
        num -= 1
        
        if switch[num] == 0:
            switch[num] = 1
        else:
            switch[num] = 0
             
        for k in range(1, num + 1):
            if 0 <= num - k < N and 0 <= num + k < N:
                if switch[num - k] == switch[num + k]:
                    if switch[num - k] == 0:
                        switch[num - k] = switch[num + k] = 1
                    else:
                        switch[num - k] = switch[num + k] = 0

                else: 
                    break
    

for i in range(0, N, 20):
    print(*switch[i : i+20])
