# 빙고 어캐함 ..  ? 오목 처럼 해보려다가 none 나옴 ㅜ ㅜ 일단 냅다 코드 작성함.. ㅠ ㅠ뭐가 단단히 잘못된듯. 
bingo_lst = [list(map(int, input().split())) for _ in range(5)]
mc = [list(map(int, input().split())) for _ in range(5)]

def bingo_pan(arr1, arr2):
    cnt = 0
    for i in range(5):
        for j in range(5):
            delete_v = mc[i][j]
            bingo_lst.insert(0, bingo_lst.pop(delete_v))
            cnt += 1
    return cnt 
            
def check(arr1, arr2):   
    cnt = 0
    for i in range(5):
        for j in range(5):
            delete_v = mc[i][j]
            bingo_lst.insert(0, bingo_lst.pop(delete_v))
            cnt += 1
            
    di = [0, 1, 1, 1]
    dj = [1, 0, 1, -1]   
    for i in range(5):
        for j in range(5):   
            bingo_cnt = 0 
            for k in range(4):
                bingo1 = 0
                for l in range(5):
                    ni = i + di[k] * l
                    nj = j + dj[k] * l
                    if not (0 <= ni < 5 and 0 <= nj < 5):
                        break 
                    if bingo_lst[ni][nj] == 0:
                        bingo1 += 1
                if bingo1 == 5:
                    bingo_cnt += 1
            if bingo_cnt == 3:
                return bingo_pan(arr1, arr2)


result = check(bingo_lst, mc) 
print(result)


# -------------------------------------------------
bingo_lst = [list(map(int, input().split())) for _ in range(5)]
mc = [list(map(int, input().split())) for _ in range(5)]
cnt = 0
def check(arr1, arr2):   
    global cnt
    di = [0, 1, 1, 1]
    dj = [1, 0, 1, -1]  
    for i in range(5):
        for j in range(5):
            delete_v = arr2[i][j]
            for r in range(5):
                for c in range(5):
                    if arr1[r][c] == delete_v:
                        cnt += 1
                        arr1[r][c] = 0
                        break
            bingo_cnt = 0 
            for k in range(4):
                bingo1 = 0
                for l in range(5):
                    ni = i + di[k] * l
                    nj = j + dj[k] * l
                    if not (0 <= ni < 5 and 0 <= nj < 5):
                        break 
                    if arr1[ni][nj] == 0:
                        bingo1 += 1
                if bingo1 == 5:
                    bingo_cnt += 1
            if bingo_cnt >= 3:
                return cnt
            
  

result = check(bingo_lst, mc) 
print(result)

뭔가 안돼 ㅜ ㅜ///..
