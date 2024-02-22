def group_word_checker(word):
    global result
    char_set = {word[0]}  # 알파벳 검사할 셋

    for j in range(1, len(word)):
        if word[j] != word[j - 1]:       # 현재 알파벳과 그 앞 알파벳이 다를때
            if word[j] not in char_set:  # 이미 앞에서 나왔던 알파벳인지 셋에서 찾아보고
                char_set.add(word[j])    # 없으면 셋에 추가
            else:                        # 있으면 그룹단어가 아니므로 return
                return
    result += 1
#-------------------함수--------------------------------------

result = 0

for i in range(int(input())):
    N = input()
    group_word_checker(N)

print(result)
