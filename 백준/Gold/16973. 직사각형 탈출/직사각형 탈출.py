from collections import deque as d

def find_four_point(H, W, r, c):
    return (r, c, r + H, c + W)


def check_bound(n, m, r, c):
    return 0<=r<=n and 0<=c<=m


def init_pre(N, M, b, hor, ver):
    for i in range(N):
        for j in range(M):
            if b[i][j] == -1: continue
            else:
                hor[i + 1][j] = hor[i][j] + 1
                ver[i][j + 1] = ver[i][j] + 1


def init_variable(li):
    for i in range(len(li)):
        li[i] -= 1

    return li

def check_init(h, w, r, c, b):
    for i in range(r, h + r):
        for j in range(c, c + w):
            if b[i][j] == 1:
                return True

    return False


def solution():
    answer = 0

    N, M = map(int, input().split())

    visit_answer = [[0] * (M) for _ in range(N)]
    board = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                visit_answer[i][j] = -1
                board[i][j] = -1

    pre_hor = [[0] * (M + 1) for _ in range(N + 1)]
    pre_ver = [[0] * (M + 1) for _ in range(N + 1)]
    init_pre(N, M, board, pre_hor, pre_ver)

    H, W, s_r, s_c, f_r, f_c = map(int, input().split())
    s_r, s_c, f_r, f_c = init_variable([s_r, s_c, f_r, f_c])

    # print(H, W, s_r, s_c, f_r, f_c)

    # 시작지점에 벽이 있는지 확인
    if check_init(H, W, s_r, s_c, board):
        return -1

    # 갈길을 구해야한다.
    # 방문 했으면 안가고
    # 방문 안했으면 갈 수 있는 곳인지 체크 누적 합을 통해 해당 영역이 나의 변이 갈 수 있는지 체크한다.
    # 갈수 있으면 방문 체크 후 이동

    que = d()
    que.append(find_four_point(H, W, s_r, s_c))
    visit_answer[s_r][s_c] = 1
    while que:
        # print(que[0])
        c_sr, c_sc, c_fr, c_fc = que.popleft()

        #위로
        if check_bound(N, M, c_sr - 1, c_sc):
            n_sr = c_sr - 1
            if visit_answer[n_sr][c_sc] == 0 and pre_ver[n_sr][c_fc] - pre_ver[n_sr][c_sc] == W:
                que.append(find_four_point(H, W, n_sr, c_sc))
                visit_answer[n_sr][c_sc] = visit_answer[c_sr][c_sc] + 1
        #왼쪽으로
        if check_bound(N, M, c_sr, c_sc - 1):
            n_sc = c_sc - 1
            if visit_answer[c_sr][n_sc] == 0 and pre_hor[c_fr][n_sc] - pre_hor[c_sr][n_sc] == H:
                que.append(find_four_point(H, W, c_sr, n_sc))
                visit_answer[c_sr][n_sc] = visit_answer[c_sr][c_sc] + 1
        #아래로
        if check_bound(N, M, c_fr + 1, c_sc):
            # print(visit_answer[c_sr + 1][c_sc] , pre_ver[c_fr][c_fc] , pre_ver[c_fr][c_sc], c_fc, c_fc, c_sc)
            if visit_answer[c_sr + 1][c_sc] == 0 and pre_ver[c_fr][c_fc] - pre_ver[c_fr][c_sc] == W:
                que.append(find_four_point(H, W, c_sr + 1, c_sc))
                visit_answer[c_sr + 1][c_sc] = visit_answer[c_sr][c_sc] + 1
        #오른쪽으로
        if check_bound(N, M, c_sr, c_fc + 1):
            if visit_answer[c_sr][c_sc + 1] == 0 and pre_hor[c_fr][c_fc] - pre_hor[c_sr][c_fc] == H:
                que.append(find_four_point(H, W, c_sr, c_sc + 1))
                visit_answer[c_sr][c_sc + 1] = visit_answer[c_sr][c_sc] + 1
    # print(*pre_ver, sep='\n')
    # print()
    # print(*pre_hor, sep='\n')
    # print()
    # print(*visit_answer, sep='\n')
    return -1 if visit_answer[f_r][f_c] == 0 else visit_answer[f_r][f_c] - 1


print(solution())
