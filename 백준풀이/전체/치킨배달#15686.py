from collections import deque as d
import sys

input = sys.stdin.readline

#입력
#1. 치킨집의 위치와 집의 위치를 따로 저장한다.
#2. 치킨집에서 M개를 선택한 조합을 만든다.
#2. 조합에 따른 치킨 거리를 구하고 그 중에 최소값을 고른다.
#3. 조합으로 구한 list를 각각 조합해서 가장 가까운 곳을 그 집에서의 치킨거리로 잡는다
#3. 총합을 구하고 그 조합이 가지는 가장 작은 치킨거리를 return 한다.
#4. 모든 경우의 최솟값을 출력한다.

N, M = map(int, input().split())
maps = []
for i in range(N):
    maps.append(input().split())

homes = []
chicks = []
for i in range(N):
    for j in range(N):
        if maps[i][j] == '1':
            homes.append((i, j))
        elif maps[i][j] == '2':
            chicks.append((i, j))


order = [(0,1), (1,0), (0,-1), (-1,0)]
def calc_chic(chic):
    rtn = [20000] * (len(homes))
    for i in range(len(homes)):
        hr, hc = homes[i]
        chic_len = 20000
        for j in chic:
            cr, cc = j
            chic_len = min(chic_len, abs(cr - hr) + abs(cc - hc))
            rtn[i] = min(rtn[i], chic_len)
    return sum(rtn)


def make_comb(chic, m, n, comb):
    min_n = 20000
    if n == m:
        return calc_chic(list(map(lambda x: chic[x], comb)))
    if n < m:
        for i in range(comb[-1] + 1, len(chic)):
            comb.append(i)
            min_n = min(min_n, make_comb(chic, m, n + 1, comb))
            comb.pop()
        return min_n

min_n = 20000
for i in range(len(chicks)):
    min_n = min(min_n, make_comb(chicks, M, 1, [i]))

print(min_n)
