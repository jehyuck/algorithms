import sys

input = sys.stdin.readline



def solution():
    N, d, k, c = map(int, input().split())

    answer = 0
    board = [int(input()) for _ in range(N)]
    for i in range(k):
        board.append(board[i])

    for i in range(len(board) - k):
        temp = set(board[i:i + k])
        temp.add(c)
        answer = max(answer, len(temp))
    return answer


print(solution())
