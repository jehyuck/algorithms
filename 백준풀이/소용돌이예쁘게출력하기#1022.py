#입력
r1, c1, r2, c2 = map(int,input().split())

#값들을 하나하나 구한다.
#1. 몇번째 칸(사각형의 층 = n)인지 구한다.

#2. 좌표가 lower에 있는지 upper에 있는지 구한다.
#2-1 upper면 시작점을 기준으로 차이를 더해준다.
#2-2 lower면 끝점을 기준으로 차이를 빼준다.

#4. 구해야하는 모든 좌표에 이것을 반복해준다.

#2 lower upper 구하는 함수
def is_upper(p):
    if p[0] > p[1]:
        return False
    else:
        return True

#1부터 2까지의 함수

def findValue(r,c):
    #0,0 예외처리
    if (r,c) == (0,0):
        return 1
    #n,n예외처리
    startFloor = max(abs(r),abs(c))
    if (r,c) == (startFloor, startFloor):
        return (startFloor * 2 + 1) ** 2

    if is_upper([r,c]):
        startV = (startFloor * 2 - 1) ** 2 + 1
        startP = (startFloor - 1, startFloor)
        return startV + abs(r - startP[0] + c - startP[1])
    else:
        lastV = (startFloor * 2 + 1) ** 2
        return lastV + (r - startFloor + c - startFloor)

#4 전부 반복
answerLine = []
for i in range(r1, r2 + 1):
    temp = []
    for j in range(c1, c2 + 1):
        temp.append(findValue(i, j))
    answerLine.append(temp)
#예쁘게출력
maxValue = max(map(max,answerLine))
printSize = len(str(maxValue))

for i in answerLine:
    for j in i:
        printV = str(j)
        if len(printV) == printSize:
            print(printV, end=' ')
        else:
            printV = " "*(printSize - len(printV)) + printV
            print(printV, end=' ')

    print()