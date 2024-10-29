import sys

input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def checkBound(n, nr, nc):
    return nr < 0 or nr >= n or nc < 0 or nc >= n

def find_consumer(n, b, t, ps):
    dist = 0
    visit = set()
    que = [t]
    visit.add(t)

    if t in ps:
        return 0, t, True
    hubo = []

    while que and not hubo:
        temp = []
        dist += 1
        for ele in que:
            cr, cc = ele
            # print(ele)
            for d_ in range(4):
                nr = cr + dr[d_]
                nc = cc + dc[d_]

                if checkBound(n, nr, nc):
                    continue
                if b[nr][nc] == 1: continue
                nt = (nr, nc)
                # print(nt)
                if nt in visit: continue
                if nt in ps:
                    hubo.append(nt)
                visit.add(nt)
                temp.append(nt)
        que = temp

    if hubo:
        hubo.sort()
        return dist, hubo[0], True
    else:
        return -1, (-1, -1), False


def imposible():
    print(-1)


def move_target(n, b, t, target):
    dist = 0
    visit = set()
    que = [t]

    visit.add(t)
    # print(t, target)
    while que:
        temp = []
        dist += 1
        for ele in que:
            cr, cc = ele
            for d_ in range(4):
                nr = cr + dr[d_]
                nc = cc + dc[d_]

                if checkBound(n, nr, nc):
                    continue
                if b[nr][nc] == 1: continue

                nt = (nr, nc)
                if nt in visit: continue
                # print(nt)
                if nt == target:
                    return dist
                visit.add(nt)
                temp.append(nt)
        que = temp
    return -1


def solution(board, n, m, f, t, p):
    possible = True
    # print(t)
    while possible and len(p):
        dist, target, possible = find_consumer(n, board, t, p)
        if not possible and len(p):
            imposible()
            return
        # print("{} -> {}".format(t, target), end=" ")
        t = target
        f -= dist
        # print(f)
        if f < 0:
            imposible()
            return

        dist = move_target(n, board, t, p[t])
        if dist == -1:
            imposible()
            return

        # print("{} -> {}".format(t, p[t]), end=" ")

        f -= dist
        if f < 0:
            imposible()
            return

        tt = p[t]
        p.pop(t)
        t = tt

        # print(f)
        f += dist * 2

    if len(p):
        imposible()
        return
    print(f)


def start():
    N, M, f = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    taxi = tuple(map(lambda x: int(x) - 1, input().split()))
    # print(*board, sep="\n")
    # 고객을 list로 관리.bfs 돌려보면서 map에서 체크하면됨
    passenger = dict()
    for i in range(M):
        a, b, c, d = map(lambda x: int(x) - 1, input().split())
        passenger[(a, b)] = (c, d)

    solution(board, N, M, f, taxi, passenger)

start()