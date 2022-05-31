import sys
from collections import deque as d
input = sys.stdin.readline
N, S, E, M = map(int, input().split())
INF = -float('inf')
dist = [INF] + [INF for _ in range(N)]
adj = [[]] + [[] for _ in range(N)]
path = [1] + [1] * N

for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a].append([b, c])

earn = tuple(map(int, input().split()))
dist[S] = earn[S]

for i in range(N):
    for j in range(len(adj[i])):
        for k in range(N):
            if adj[i][j][0] == k:
                adj[i][j][1] = earn[k] - adj[i][j][1]


def bellman():
    rtn = 0
    for i in range(1, N + 1):
        for crt in range(N):
            for j in range(len(adj[crt])):
                rear, cost = adj[crt][j]
                # print(crt, rear,dist[rear], dist[crt] + cost)
                if dist[rear] < dist[crt] + cost:
                    dist[rear] = dist[crt] + cost
                    if i == N:
                        if is_incircle(crt, E):
                            return 1
    return rtn


def is_incircle(start, end):
    visit = [0] * N
    visit[start] = 1
    que = d([start])
    while que:
        crt = que.popleft()
        # print(i, crt)
        if crt == end:
            return 1
        visit[crt] = 1
        for j in adj[crt]:
            if visit[j[0]] != 1:
                que.append(j[0])
    return 0
#
#
is_in = bellman()
#
# print(earn, dist, path, adj)
if dist[E] == INF:
    print('gg')
elif is_in:
    print('Gee')
else:
    print(dist[E])
