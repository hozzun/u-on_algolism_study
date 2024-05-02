def solution(weights):
    answer = 0
    dic = {}
    cal = [1.5, 2, 4/3]
    for i in weights:  # 딕셔너리로 전환
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    print(dic)
  
    for key, val in dic.items():
        if val > 1:     # 중복인 경우
            answer += val*(val-1)//2
        for k in cal:   # 아닌 경우
            if key * k in dic:
                answer += 1
    
    return answer
