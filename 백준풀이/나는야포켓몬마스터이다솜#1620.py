import sys
input = sys.stdin.readline

N, M = map(int, input().split())

No = [0]
dic = {}
for i in range(N):
    poke = input().strip()
    No.append(poke)
    dic[poke] = i + 1

for j in range(M):
    query = input().strip()
    if query.isdigit():
        a = int(query)
        print(No[a])
    else:
        print(dic[query])
