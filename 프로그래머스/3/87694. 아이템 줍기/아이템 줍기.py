def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    board = [[0] * 102 for _ in range(102)]
    # visit = [[0] * 51 for _ in range(51)]
    # 지형을 그린다.
    fillRects(board, rectangle)
    
    cy = characterY * 2
    cx = characterX * 2
    iy = itemY * 2
    ix = itemX * 2
    
    # 너비우선 탐색을 통해 나아간다.
    que = [(cy, cx)]
    board[cy][cx] = 0
    board[iy][ix] = -1
    
    answer = bfs(board, que)

    return answer

def bfs(board, que):
    rtn = 0
    
    dr = (0, 1, -1, 0)
    dc = (1, 0, 0, -1)
    
    while que:
        tempQue = []
        for node in que:
            r, c = node
            if board[r][c] == -1:
                return rtn // 2
            for d_ in range(4):
                nr = dr[d_] + r
                nc = dc[d_] + c
                
                if checkBound(nr, nc, 102, 102):
                    continue  
                    
                if board[nr][nc] == -1:
                    tempQue.append((nr, nc))
                    
                if not board[nr][nc] == 1:
                    continue
                    
                board[nr][nc] = 0
                tempQue.append((nr, nc))
                
        que = tempQue
        rtn += 1
        
    return -1

def checkBound(nr, nc, N, M):
    return not (0 <= nr < N and 0 <= nc < M)

def fillRects(board, rects):
    for rect in rects:
        fillLine(board, rect)
    for rect in rects:
        fillRect(board, rect)
    
def fillLine(board, rect):
    c1, r1, c2, r2 = map(lambda x: x * 2, rect)
    
    # 경계선을 칠한다.
    for i in range(c1, c2 + 1):
        board[r1][i] = 1
    
    # 경계선을 칠한다.
    for i in range(c1, c2 + 1):
        board[r2][i] = 1
    
    # 경계선을 칠한다.
    for i in range(r1, r2 + 1):
        board[i][c2] = 1
        
    # 경계선을 칠한다.
    for i in range(r1, r2 + 1):
        board[i][c1] = 1
    
    
def fillRect(board, rect):
    c1, r1, c2, r2 = map(lambda x: x * 2, rect)
    
    # 전부 벽으로 칠한다.
    for i in range(r1 + 1, r2):
        for j in range(c1 + 1, c2):
            board[i][j] = 0
    
    
    