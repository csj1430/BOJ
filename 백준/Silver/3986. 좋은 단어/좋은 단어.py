# 열품타 9분에 시작

n = int(input())
good = 0 # 좋은 단어 개수 저장할 변수

for _ in range(n) :
    word = list(input())
    stack = []
    pairs = 0 # 쌍 개수 저장할 변수

    for i in range(len(word)) :
        if not stack : # 스택이 비어 있다면
            stack.append(word[i]) 

        elif stack[-1] == word[i] : # 스택의 탑이 현재 문자와 같다면
            stack.pop()
            pairs += 1

        else :
            stack.append(word[i]) 

    if pairs == len(word) // 2 and not stack :
        good += 1

print(good)