from itertools import combinations as c

#입력받기
n, m = list(map(int, input().split(' ')))
cards = list(map(int,input().split(' ')))

#모듈을 이용하여 카드 index로 조합을 한다.
order = c(range(n), 3)

#모든 조합값에 대해서 목표값 m과의 차이에 대해 최솟값을 기록한다
minn = float('inf')
백준 #2798 블랙잭
for i in list(order):
    sumall = cards[i[0]]+cards[i[1]]+cards[i[2]]

    crtResult = m - sumall
    if crtResult == 0:
        minn = 0
        break

    if crtResult >= 0 and crtResult < minn:
        minn = crtResult
print(m - minn)