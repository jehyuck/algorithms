#입력최적화
import sys
input = sys.stdin.readline

#입력
n, limit = map(int,input().split())

#(무게,가치)
items = []
for i in range(n):
    w, v = map(int, input().split())
    items.append((w, v))

items.sort(key=lambda x: x[0])
items = [0] + items

#dp를 이용한 배낭체우기
#1. 무게가 작은 순서로 정렬 한다.
#2. i번째 물품을 선택하고
#3. 무게를 1씩 더하면서 이전 물품의 경우와 비교한다.
#3-1.물품을 넣을 수 없다면 이전의 물품의 최적값을 가져온다.
#3-2 넣는 것(p[i-1][w-w_i]) 넣지 않는것(p[i-1][w])와 비교해
#   더 큰 값(p[i][w])을 그 위치에 기록한다.
#4. 2-3을 모든 물품에 반복한다.

dp = [[0 for _ in range(limit+1)] for _ in range(n+1)]

for i in range(1,n+1):
    w, v = items[i]

    for j in range(limit+1):
        #3-1
        if w > j:
            dp[i][j] = dp[i-1][j]
        else:
        #3-2
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w] + v)

print(dp[-1][-1])

"""
간단한 배낭체우기문제
1.무게가 10만이고 n이 100이라 O(limit*n)의 시간복잡도를 가진다.
--> 파이썬으로 제출할 시 오래걸림

"""