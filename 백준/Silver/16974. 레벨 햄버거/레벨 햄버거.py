
def dfs(N, X, bread, petty):
    if N == 0:
        if X == 0:
            return 0
        else:
            return 1

    if X == 1:
        return 0

    if 1 < X <= bread[N - 1] + 1: return dfs(N - 1, X - 1, bread, petty)

    if X == bread[N - 1] + 2: return petty[N - 1] + 1

    if X <= bread[N - 1] * 2 + 2: return petty[N - 1] + 1 + dfs(N - 1, X - bread[N - 1] - 2, bread, petty)

    return petty[N]



def solution():
    answer = 0

    N, X = map(int, input().split())

    dp_bread = [0] * 51
    dp_petty = [0] * 51

    dp_bread[0], dp_petty[0] = 1, 1
    for i in range(1, N):
        dp_petty[i] = dp_petty[i - 1] * 2 + 1
        dp_bread[i] = dp_bread[i - 1] * 2 + 3


    answer = dfs(N, X, dp_bread, dp_petty)
    return answer


print(solution())
