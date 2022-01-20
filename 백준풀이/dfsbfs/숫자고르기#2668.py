#입력
import sys
input = sys.stdin.readline

N = int(input())

inputlist = [0] + [int(input()) for _ in range(N)]
visit = [0] + [0 for _ in range(N + 1)]
answerset = set()
#dfs를 이용한 방향그래프 사이클 탐색
#1. 전부다 방문할 때 까지 노드를 탐색한다.
#2. 상태를 방문 했던곳(-2), 방문 한 곳(-1), 방문 안한 곳(0)으로 설정한다.
#2-1. 방문 했던곳을 방문시 dfs를 종료
#2-2. 방문 한 곳을 방문 시 answer 리스트에 본이이 또 나올 때 까지 전부 방문 했던곳(-2)으로 처리한다.
#2-3. 방문 안 한 곳을 방문 시 방문 한곳(-1)으로 처리하고 방문한다.


def dfs(node):
    if visit[node] == -2:
        return

    elif visit[node] == -1:
        visit[node] = -2
        answerset.add(node)
        dfs(inputlist[node])

    elif visit[node] == 0:
        visit[node] = -1
        dfs(inputlist[node])

    visit[node] = -2
    return

for i in range(1, N+1):
    if visit[i] == 0:
        dfs(i)

print(len(answerset), *sorted(list(answerset)), sep="\n")

"""
dfs를 이용해 방향그래프의 싸이클을 찾는 문제
"""