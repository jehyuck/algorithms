from collections import deque as dd


def move(start, target):
    tr, tc = target
    sr, sc = start
    ddr = tr - sr
    ddc = tc - sc
    dr = 0 if ddr == 0 else -1 if ddr < 0 else 1
    dc = 0 if ddc == 0 else -1 if ddc < 0 else 1
    if dr == 0 and dc == 0:
        return False
    if dr != 0:
        return (sr + dr, sc)
    return (sr, sc + dc)
def p2i(p):
    return [p[0] - 1, p[1] - 1]


def init_robots(dp, p, routes):
    rtn = []
    answer = 0
    visit = [[0] * 100 for _ in range(100)]
    for r in routes:
        first = p2i(p[r[0] - 1])
        root = dd()
        cr, cc = first
        visit[cr][cc] += 1
        if visit[cr][cc] == 2:
            answer += 1
        for i in range(1, len(r)):
            root.append(p2i(p[r[i] - 1]))
        robot = [first, root]
        rtn.append(robot)
    return rtn, answer


def move_check(d):
    if len(d) == 0: return False
    for i in d:
        if i[1]:
            return True
    return False


def erase_board(board, eraseque):
    e_iter = iter(eraseque)
    for _ in range(len(eraseque)):
        r, c = e_iter.__next__()
        board[r][c] = 0

        
def solution(points, routes):
    dp_root = dict()
    board = [[0 for _ in range(100)] for _ in range(100)]
    robots, value = init_robots(dp_root, points, routes)
    answer = value
    eraseque = set()
    while move_check(robots):
        erase_board(board, eraseque)
        temp = []
        eraseque = set()
        for r in robots:
            sr, n = r
            if not n: continue
            m = move(sr, n[0])
            if m == False:
                n.popleft()
                if not n: continue
                m = move(sr, n[0])
                if m == False:
                    continue
            r[0] = m
            nr, nc = r[0]
            board[nr][nc] += 1
            if board[nr][nc] == 2:
                answer += 1
            eraseque.add(r[0])
            temp.append(r)
        robots = temp
            
    
    return answer