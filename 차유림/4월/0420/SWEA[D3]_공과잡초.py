# 실패버전 ㅠㅠ! 테케 막 53개?만 맞았대ㅠ

# T = int(input())
# for tc in range(1, T+1):
#     S = str(input())
#     ball = ['(|', '|)', '()']
#     ball_cnt = 0
#     for i in ball:
#         if i in S:
#             ball_cnt += 1
    
#     print(f"#{tc} {ball_cnt}")



# 성공버전 
# 44988 kb 112 ms 코길 194

T = int(input())
for tc in range(1, T+1):
    S = input()
    ball = ['(|', '|)', '()'] # 이거 하나하나하나가 공임! 공이라 생각해서 세줬음
    ball_cnt = S.count(ball[0]) + S.count(ball[1]) + S.count(ball[2])
    
    print(f"#{tc} {ball_cnt}")





