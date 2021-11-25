#입력
n = int(input())
pickstack = [-1 for _ in range(n)]
answer = 0
visited = [False] * n
#유망 체크
def checkAppend(y,x):
    for i in range(y):
        if y - i == abs(x - pickstack[i]):
            return False
    return True

def nQueen(F, N):
    global answer
    if F == N:
        answer += 1
        return

    for i in range(N):
        if visited[i]:
            continue
        pickstack[F] = i
        if checkAppend(F, i):
            visited[i] = True
            nQueen(F+1, N)
            visited[i] = False

nQueen(0, n)

print(answer)

"""def checkAppend(y,x):
    for i in range(y):
        if pickstack[i] == x or (y - i) == (x - pickstack[i]) or (y - i) == (pickstack[i] - x):
            return False
    return True
"""