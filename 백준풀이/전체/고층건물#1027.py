#입력
n = int(input())

apts = [0] + list(map(int, input().split(' ')))


#보이는 것들을 반환하는 함수
# 인덱스가 작은쪽은 기울기가 커지는 지점에서 안보인다
# 인덱스가 큰 쪽은 기울기가 작아지는 지점에서 안보인다
def canSeeCount(index):
    leftMin = float('inf')
    rightMax = -float('inf')
    rtn = 0
    seeIndex = index - 1

    #왼쪽을 봤을 때 기울기가 더 작아져야한다.
    while seeIndex > 0:
        a = index - seeIndex
        b = apts[index] - apts[seeIndex]
        g = b/a

        if g < leftMin:
            rtn += 1
            leftMin = g

        seeIndex -= 1

    #오른쪽을 봤을때 기울기가 점점 커져야 한다.
    seeIndex = index + 1
    while seeIndex < n+1:
        a = seeIndex - index
        b = apts[seeIndex] - apts[index]
        g = b/a
        if g > rightMax:

            rtn += 1
            rightMax = g

        seeIndex += 1

    return rtn

#모든 위치에서 탐색함수를 실행한다.
answer = 0
for i in range(1,len(apts)):
    answer = max(answer,canSeeCount(i))

#출력
print(answer)