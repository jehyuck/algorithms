#숫자 갯수 입력
n = int(input())

#정방향으로 문제 입력 받고, 역방향 따로 만들기
numbers = list(map(int,input().split()))
rNumbers = list(reversed(numbers))

#정방향과 역방향 dp
dp1 = [1]*n
dp2 = [1]*n

#n개 만큼을 동적계획법으로 실행, 자기보다 작은 것들 중 가장 큰 것을 고른다
for i in range(n):
    maxV1 = 1
    maxV2 = 1

    for j in range(i):
        #정방향 최댓값 구하기
        if numbers[j] < numbers[i]:
            maxV1 = max(dp1[j] + 1, maxV1)
        #역방향 최댓값 구하기
        if rNumbers[j] < rNumbers[i]:
            maxV2 = max(dp2[j] + 1, maxV2)

    dp1[i] = maxV1
    dp2[i] = maxV2
dp2.reverse()

#둘다 같은 방향으로 바꾼뒤 같은 i 번째의 합 중
#최댓값에서 1을 빼준 후(겹치는 부분이 두번 더해져서) 출력
dp3 = []
for i in range(n):
    dp3.append(dp1[i] + dp2[i])


#출력
print(max(dp3)-1)
