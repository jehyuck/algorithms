#입력 최적화
import heapq as h
import sys
input = sys.stdin.readline

#입력
N = int(input())

limitsort = []
for _ in range(N):
    limitsort.append(tuple(map(int,input().split())))

limitsort.sort()

#우선순위 큐를 이용한 스케줄링
#1.입력을 전부받고 과제마감일을 내림차순으로 정렬한다.
#2.과제 마감일이 제일 늦은 날을 기준으로
#2-1. 과제 마감이 이상인 과제들을 우선순위 큐에 집어넣는다.
#2-2. 점수가 가장 높은 것을 현재 마감일에 채우고 마감일을 1낮춘다.
#3. 마감일이 1일때를 채우게 되면(현재시간이 0이 되면) 종료한다.

heap = []
crt = limitsort[-1][0]
answer = 0

while crt != 0:
    # print(crt, limitsort)
    # 2-1. 과제 마감이 이상인 과제들을 우선순위 큐에 집어넣는다.
    if limitsort:
        while limitsort and limitsort[-1][0] >= crt:
            work = limitsort.pop()
            h.heappush(heap, (-work[1], work[0]))
    if heap:
        # print(heap)
        a = h.heappop(heap)
        # print(a, crt)
        answer += a[0]
        # print()

    crt -= 1

print(-answer)

"""
우선순위 큐를 이용한 기본적인 스케줄링 알고리즘
"""