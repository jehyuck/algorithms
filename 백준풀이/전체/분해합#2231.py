#입력을 받는다.
n = input()

#답 변수를 0으로 초기설정, 최소 최대 범위를 구하기 위해 길이를 입력한다.
nLen = len(n)
answer = 0

#비교를 위해 n을 int로 바꾸어준다.
n = int(n)

#최대 최소 범위
minX = n - nLen * 9 if n - nLen * 9 > 0 else 0
maxX = n - nLen * 1 if n - nLen * 1 > 0 else 0

#각자리수 합을 n과 비교해 구하면 바로 탈출한다.
for i in range(minX, maxX+1):
    sumX = i + sum(map(int,str(i)))
    if sumX == n:
        answer = i
        break

print(answer)