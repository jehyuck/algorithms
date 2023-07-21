
def dfs(start, end, s, n):
    dfs_n = 3 ** (n - 1)
    if n == 0 or start > end:
        return

    dfs(start, start + dfs_n, s, n - 1)
    for i in range(start + dfs_n, start + dfs_n * 2):
        s[i] = " "
    dfs(start + dfs_n * 2,  dfs_n * 3 + end, s, n - 1)

def solution():
    while True:

        try:
            inp = input()
            if inp == "":
                break
            n = int(inp)
            answer = ["-"] * (3 ** n if n != 0 else 0 + 1)
            dfs(0, 3**n, answer, n)
            print(''.join(answer))

        except EOFError:
            break

solution()

