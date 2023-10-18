import sys
from collections import deque as d

input = sys.stdin.readline

def solution():
    answer = 0

    N, M = map(int, input().split())

    visit = [False] * 101
    ladder = dict()
    snake = dict()
    que = d()
    for i in range(N):
        x, y = map(int, input().split())
        ladder[x] = y

    for j in range(M):
        u, v = map(int, input().split())
        snake[u] = v

    que.append(1)

    visit[0] = True
    visit[1] = True
    while True:
        answer += 1
        temp = d()
        for crt in que:
            for d_ in range(1, 7):
                nd_ = crt + d_

                if nd_ > 100: break
                if visit[nd_]: continue
                visit[nd_] = True
                if nd_ in ladder:
                    nd_ = ladder[nd_]
                    visit[nd_] = True
                elif nd_ in snake:
                    nd_ = snake[nd_]
                    visit[nd_] = True
                if nd_ == 100:
                    return answer
                temp.append(nd_)

        que = temp

    return answer
print(solution())