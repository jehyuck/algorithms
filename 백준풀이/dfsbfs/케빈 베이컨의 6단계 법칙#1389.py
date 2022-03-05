import sys
from collections import deque as d

input = sys.stdin.readline

N, E = map(int, input().split())

adj = [[0]] +[[] for _ in range(N)]

for _ in range(E):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
#최단거리 알고리즘의 총합
#1. 인접리스트를 구한다.
#2. N개의 노드들에 대해 모든 최단거리 알고리즘을 돌린다.
#2. n의 인접리스트의 값들로 list를 update가능 한 것만 queue에 넣는다.
#2. queue전부 다 초기화 될 때까지 한다.
#2. 끝나면 총 합을 더한다.
#3. 총합중 가장 작은 것을 답으로 출력한다.

answer = 0
min_v = 5051
for i in range(1, N + 1):
    count = 0
    dist = [0] + [5051] * N
    dist[i] = 0
    queue = d([i])
    while queue:
        crt = queue.popleft()
        for j in adj[crt]:
            if dist[crt] + 1 < dist[j]:
                queue.append(j)
                dist[j] = dist[crt] + 1
    temp = sum(dist)
    if min_v > temp:
        answer = i
        min_v = temp

print(answer)