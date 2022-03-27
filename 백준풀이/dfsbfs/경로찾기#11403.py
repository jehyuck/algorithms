import sys
from collections import deque as d
input = sys.stdin.readline

#bfs
#1. 인접행렬을 전부 구한다. 한줄에 해당하는 visit을 구한다.
#2. 한 줄에 대해 방문을 안했다면 que에 넣는다.
#2. que가 전부 빌 때까지 방문한다.
#2. 정답에 visit배열을 추가한다.
#3. visit을 출력한다.

N = int(input())
maps = []
adj_n = []
for _ in range(N):
    temp = tuple(map(int, input().split()))
    maps.append(temp)
    adj_temp = []
    for i in range(N):
        if temp[i] == 1:
            adj_temp.append(i)
    adj_n.append(adj_temp)

answer = []
for i in range(len(adj_n)):
    visit = [0] * N
    que = d(adj_n[i])
    while que:
        crt = que.pop()
        if visit[crt] == 1:
            continue
        visit[crt] = 1
        for j in range(len(adj_n[crt])):
            if visit[adj_n[crt][j]] == 0:
                que.append(adj_n[crt][j])
    answer.append(visit)

for i in answer:
    print(*i)