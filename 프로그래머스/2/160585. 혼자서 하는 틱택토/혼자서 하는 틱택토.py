dr = (-1, -1, -1, 0, 0, 1, 1, 1)
dc = (-1, 0, 1, -1, 1, -1, 0, 1)


def charactorCount(board):
    gameCount = sum(map(lambda x: x.count("O"), board)) - sum(map(lambda x: x.count("X"), board))
    return gameCount > -1 and gameCount < 2


def findPoint(board):
    x = []
    o = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                o.append((i, j))
            elif board[i][j] == 'X':
                x.append((i, j))
    return o, x


def checkBound(nr, nc):
    return nr < 0 or nr >= 3 or nc < 0 or nc >= 3


def checkGame(board):
    global dr, dc
    for i in range(3):
        for j in range(3):
            if board[i][j] == ".": continue
            target = board[i][j]
            for d_ in range(8):
                nr = i
                nc = j
                count = 1
                for _ in range(2):
                    nr += dr[d_]
                    nc += dc[d_]
                    
                    if checkBound(nr, nc) or target != board[nr][nc]:
                        continue
                    count += 1
                if count == 3:
                    return True
                
    return False


def playGame(board, oPoint, xPoint, rr):
    if rr == len(oPoint):
        return 1
    
    for o in oPoint:
        r, c = o
        if board[r][c] != ".":
            continue
            
        board[r][c] = "O"
        if rr == len(xPoint):
            return 1
        if checkGame(board):
            board[r][c] = "."
            continue
        
        for x in xPoint:
            xr, xc = x
            
            if board[xr][xc] != ".":
                continue
            board[xr][xc] = "X"
            if checkGame(board):
                if rr + 1 == len(oPoint):
                    return 1
                board[xr][xc] = "."
                continue
            rtn = playGame(board, oPoint, xPoint, rr + 1)
            if rtn == 1:
                return 1
            
            board[xr][xc] = "."
        board[r][c] = "."
        
    return 0
    

def solution(board):
    if not charactorCount(board):
        return 0
    oPoint, xPoint = findPoint(board)
    
    return playGame([['.' for _ in range(3)] for _ in range(3)], oPoint, xPoint, 0)
