import sys
from collections import deque as d
# from collections import defaultdict as dd

input = sys.stdin.readline

def solution():
    answer = -1

    N, M = 12, 6
    board = [list(input().rstrip()) for _ in range(N)]

    # 모든 그래프를 탐색하면서 4방탐색 후 연계되는 그룹을 찾는다.
    # 연계되는 그룹을 전부 지운 뒤 해당 점을 y로 정렬한다.
    # y가 큰 순서대로 (오름 차순) 위의 값을 끌어내린다. '.'이 등장 할 때까지

    dr = (1, -1, 0, 0)
    dc = (0, 0, 1, -1)

    possible_flag = True
    while possible_flag:
        removed = []
        visit = [[False] * M for _ in range(N)]
        possible_flag = False
        answer += 1
        for i in range(N):
            for j in range(M):
                if visit[i][j]: continue
                if board[i][j] == '.': continue

                visit[i][j] = True
                target = board[i][j]

                group = d()
                group.append((i, j))

                rtn = d()

                while group:
                    r, c = group[0]
                    rtn.append(group.popleft())

                    for d_ in range(4):
                        nr = r + dr[d_]
                        nc = c + dc[d_]

                        if not check_bound(nr, nc, N, M):continue
                        if visit[nr][nc]: continue
                        if target != board[nr][nc]: continue

                        visit[nr][nc] = True
                        group.append((nr, nc))


                if len(rtn) > 3:
                    possible_flag = True
                    for ele in rtn:
                        r, c = ele
                        board[r][c] = '.'
                        removed.append(ele)

        removed.sort(key=lambda x:  x[0])
        for r, c in removed:
            nr = r
            while r > 0:
                nr -= 1

                if board[nr][c] == '.': break
                board[r][c] = board[nr][c]
                board[nr][c] = '.'
                r = nr
    return answer

def check_bound(r, c, N, M):
    return 0 <= r < N and 0<= c < M
print(solution())