#입력 최적화와 자료구조 queue가져오기
from collections import deque as q
import sys
input = sys.stdin.readline

#입력
N, M = map(int, input().split())

#위상정렬을 이용한 순서 출력
#N개의 list와 set을 만든다.
#1. 위상과 더작은 사람을 담는 list 만들기
#2-1. 비교 line을 입력 받을 때 더 작은 사람에게 기존+1의 위상을 준다.
#2-2. 더 큰사람의 list요소에 작은사람을 추가해준다.
#3. 출력- 위상이 0인 사람들을 queue에 전부 추가한다.
#3-1 popleft하여 출력하고 그 사람의 list(비교 했을 때 키가 작았던 사람)의 사람들 전부 위상을 1 낮춘다.
#3-2 list안의 사람들 중 위상이 0인 사람들을 queue의 오른쪽에 추가한다.
#4 큐가 빌 때까지 3을 반복
lowerList = [[] for _ in range(N+1)]
degree = [0 for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())

    degree[b] += 1
    lowerList[a].append(b)

#3
queue = q()
for i in range(1, 1+N):
    if degree[i] == 0:
        queue.append(i)

#3-1
while queue:
    a = queue.popleft()
    print(a, end=" ")

    for i in lowerList[a]:
        #3-1
        degree[i] -= 1
        #3-2
        if degree[i] == 0:
            queue.append(i)


"""
그래프이론의 위상정렬문제
1.bfs로 푼사람도 있으니 한번 풀오보길
"""