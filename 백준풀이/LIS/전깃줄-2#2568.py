import sys

input = sys.stdin.readline
N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]
lines.sort()
idx = [0] * len(lines)
dp = [(0, 0)]

#dp와 이분탐색 인것같음
#1. 입력을 받아 정렬한다.
#2. 현재 위치가 dp에 들어갈 위치를 이분탐색으로 구한다.
#3. 위치의 값을 빼내면서 answer에 추가하고 dp에는 현재 값을 넣는다.
#4. 집어 넣을 때마다 들어간 index위치를 기록한다.
#5. n == len(전기줄) --> n == 0 까지 등장하는 인덱스를 기록한다.
#5. 끝까지 이것을 반복하고 제거된 목록(list : answer)을 출력한다.



answer = []
for i in range(len(lines)):
    start = 0
    last = len(dp) - 1

    if dp[-1][1] < lines[i][1]:
        dp.append(lines[i])
    else:
        while start <= last:
            mid = (start + last) // 2

            # print(start, last, mid, dp)
            if dp[mid][1] >= lines[i][1]:
                last = mid - 1
            else:
                start = mid + 1
        dp[last + 1] = lines[i]
    idx[i] = last + 1
    # print(lines[i][1], dp[last], last, len(dp))
    # print(dp, answer)

target = len(dp) - 1
# print(idx, target)
for i in range(N - 1, -1, -1):
    if idx[i] == target:
        target -= 1
        continue
    answer.append(lines[i])

print(len(answer), *map(lambda x: x[0], sorted(answer)), sep='\n')

"""
lis를 nlogn으로 푸는 알고리즘

이전에 풀어봤지만 정확히 이해를 하지 못하고 풀어 기억이 잘 안났었다.
갯수를 빨리 구하는 방법이라 LIS자체가 정답이 아니게 변형이 된다.
그걸 바로잡기위해 갯수를 구할때 index를 기록하고 다시 순회하면서 올바른 LIS를 구해내야한다.
그부분을 빼먹어서 오답이 났었다.
"""