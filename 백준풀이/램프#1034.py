#입력
n, m = list(map(int,input().split()))

#입력 2
lamps_dict = {}

#입력된 램프점등 구조의 갯수를 count한다.
for i in range(n):
    lamps = input()
    #초기화시 0의 갯수도 초기화한다.
    if lamps not in lamps_dict:
        lamps_dict[lamps] = [lamps.count('0'), 1]
    else:
        lamps_dict[lamps][1] += 1
k = int(input())

#k값의 조건이 '0'이 카운트된 값에 만족하는 것 중 최댓값을 고른다.
answer = 0
kOdds = True if k%2 != 0 else False

for i in lamps_dict:
    dictOdds = True if lamps_dict[i][0]%2 != 0 else False
    if lamps_dict[i][0] <= k and (dictOdds == kOdds):
        if answer < lamps_dict[i][1]:
            answer = lamps_dict[i][1]

print(answer)
