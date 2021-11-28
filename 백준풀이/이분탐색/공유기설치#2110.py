#입력
n, k = list(map(int,input().split()))

#집들의 위치를 입력받음
homes = []
for i in range(n):
    homes.append(int(input()))

#집간의 거리를 기준으로 이분탐색을 하기 위해서 정렬
homes.sort()

#집간의 거리를 기준으로 이분탐색
#최솟값은 1 최댓값은 1000000000이지만 사실상 끝집과 첫집의 거리
minDist = 1
maxDist = homes[-1] - homes[0]
answer = 0
#최소거리가 최대거리보다 일치해지거나 커질 때 정답
while minDist <= maxDist:
    mid = int((minDist+maxDist)/2)
    placed = homes[0]

    crt = 1
    #몇개가 설치 가능한지 탐색
    for i in range(1, len(homes)):
        if placed + mid <= homes[i]:
            crt += 1
            placed = homes[i]

    #설치한 갯수가 적으면 mid를 키워주고
    if crt >= k:
        answer = max(mid, answer)
        minDist = mid+1
    else:
    #설치 갯수가 같거나 작으면 mid를 낮춰준다.
        maxDist = mid-1

print(answer)