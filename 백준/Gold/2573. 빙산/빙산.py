from collections import deque as d

def find_water(board, r, c, n, m):
    dr = (1, 0, -1, 0)
    dc = (0, 1, 0, -1)
    water_count = 0

    for d_ in range(4):
        nr = r + dr[d_]
        nc = c + dc[d_]

        if not check_bound(nr, nc, n, m): continue
        if board[nr][nc] == 0:
            water_count += 1

    return water_count

def find_chunk(board, i, j, n, m):
    dr = (1, 0, -1, 0)
    dc = (0, 1, 0, -1)
    visit = [[False] * m for _ in range(n)]
    visit[i][j] = True
    chunk = d()

    chunk.append((i, j))
    idx = 0
    while idx < len(chunk):
        r, c = chunk[idx]
        idx += 1

        for d_ in range(4):
            nr = r + dr[d_]
            nc = c + dc[d_]

            if not check_bound(nr, nc, n, m): continue
            if visit[nr][nc] or board[nr][nc] == 0: continue
            visit[nr][nc] = True
            chunk.append((nr, nc))

    return chunk


def check_bound(i, j, n, m):
    return 0 <= i < n and 0 <= j < m


def find_chunk_ice(board, n, m):
    count = 0

    chunk_found = False
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0:
                count += 1
                if not chunk_found:
                    chunk_found = True
                    chunk = find_chunk(board, i, j, n, m)

    if len(chunk) != count:
        return 0, []

    return count, chunk


def solution():
    answer = 0

    n, m = map(int, input().split())
    board1 = [list(map(int, input().split())) for _ in range(n)]

    count, chunk = find_chunk_ice(board1, n, m)
    board = board1

    while chunk and len(chunk) == count:
        answer += 1
        temp = d()

        que = d()
        while chunk:
            r, c = chunk.popleft()
            minus_value = find_water(board, r, c, n, m)
            v = max(0, board[r][c] - minus_value)
            que.append((r, c, v))
            if v > 0:
                temp.append((r, c))
            else:
                count -= 1

        chunk = temp
        for i in que:
            r, c, v = i
            board[r][c] = v
        # print(count, board)
        if not chunk or count != len(find_chunk(board, chunk[0][0], chunk[0][1], n, m)):
            break
    if count == 0:
        return 0
    return answer


print(solution())