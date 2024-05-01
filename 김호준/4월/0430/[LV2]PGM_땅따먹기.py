def solution(land):
    answer = 0

    # 인덱스가 겹치지 않는 다음 배열의 인덱스 값 = 이전 배열의 최대 값 + 본인으로 갱신
    for i in range(len(land)-1):
        land[i+1][0] = max(land[i][1], land[i][2], land[i][3]) + land[i+1][0]
        land[i+1][1] = max(land[i][0], land[i][2], land[i][3]) + land[i+1][1]
        land[i+1][2] = max(land[i][0], land[i][1], land[i][3]) + land[i+1][2]
        land[i+1][3] = max(land[i][0], land[i][1], land[i][2]) + land[i+1][3]

    # 마지막 배열의 최대 값 출력
    answer = max(land[-1])

    return answer
