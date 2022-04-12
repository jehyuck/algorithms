import sys
from collections import deque as d
input = sys.stdin.readline
N = int(input())

baby_shark_v = [2, 0]
baby_shark_p = None
answer = 0
sea = []
for i in range(N):
    sea.append(list(map(int, input().split())))
for i in range(N):
    if baby_shark_p == None:
        for j in range(N):
            if sea[i][j] == 9:
                baby_shark_p = [i, j]
                break
    else:
        break

#bfs
#조건
#1. 먹을 수 있는 물고리를 찾을 때 까지 bfs
#2. 먹었다면 공간을 0으로 만듬
#3. 지나온 공간은 다시 지나지 않는다.
#4. 한 마리를 먹었다면 지나온 공간을 다시 지날 수 있도록 초기화
#1. 모든 길이 막혀있다면 탈출하나.
#2. 갈 수 있는 길이 있다면 간다.

delta = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def bfs(p, v, visit):
    que = d()
    que.append((p, 0))
    visit[p[0]][p[1]] = 1
    new_list = []
    while que:
        crt_p, crt_dist = que.popleft()
        y, x = crt_p
        for dy, dx in delta:
            my, mx = dy + y, dx + x
            if 0 <= mx < N and 0 <= my < N and visit[my][mx] == 0:
                if sea[my][mx] in (0, v[0]):
                    visit[my][mx] = 1
                    que.append(((my, mx), crt_dist + 1))
                elif sea[my][mx] < v[0]:
                    new_list.append((crt_dist + 1, (my, mx), [v[0], v[1] + 1]))
    if new_list:
        new_list.sort()
        return (new_list[0])
    return 0

bool_eat = 1
while bool_eat:
    sea[baby_shark_p[0]][baby_shark_p[1]] = 0
    temp = bfs(baby_shark_p, baby_shark_v, [[0] * N for _ in range(N)])
    if temp == 0:
        bool_eat = 0
    else:
        dist, baby_shark_p, baby_shark_v = temp
        answer += dist
        if baby_shark_v[0] == baby_shark_v[1]:
            baby_shark_v = [baby_shark_v[0] + 1, 0]

print(answer)


