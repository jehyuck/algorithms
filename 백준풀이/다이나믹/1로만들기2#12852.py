from collections import deque as d
N = int(input())

#bfs
#1. N개의 list를 만든다
#2. 각각의 연산에 대해 n번째 값에 저장한다.
#2. n번째 칸이 차 있으면 pass
#2. 비어있으면 기존의 값을 이어서 저장하고 n을 que에 넣는다
#3. 1에 닿으면 그즉시 종료하고 출력

que = d([N])
mem = [[]] * N + [[]]
while que:
    crt = que.popleft()
    path = mem[crt]
    if crt == 1:
        break
    a, b = divmod(crt, 3)
    if b == 0 and mem[a] == []:
        que.append(a)
        mem[a] = path + [crt]
    a, b = divmod(crt, 2)
    if b == 0 and mem[a] == []:
        que.append(a)
        mem[a] = path + [crt]
    if mem[crt - 1] == []:
        que.append(crt - 1)
        mem[crt - 1] = path + [crt]

print(len(mem[1]))
print(*mem[1], 1)