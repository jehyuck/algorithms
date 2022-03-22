import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

query = []
crt = input()


while crt != '':
    query.append(int(crt))
    crt = input()


def post(s, e):
    if s > e:
        return

    root = query[s]
    i = s + 1

    while i <= e:
        if query[i] > root:
            break
        i += 1

    post(s + 1, i - 1)
    post(i, e)
    print(root)


post(0, len(query) - 1)