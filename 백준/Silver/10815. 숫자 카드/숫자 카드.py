n = int(input())
input1 = input()
have = set(map(int, input1.split())) # 가지고 있는 카드들

m = int(input())
input2 = input()
input_cards = list(map(int, input2.split())) # 확인할 카드들

for card in input_cards :
    if card in have :
        print(1, end=' ')
    else :
        print(0, end=' ')