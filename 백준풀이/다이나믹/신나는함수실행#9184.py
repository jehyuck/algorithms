#입력
import sys
input = sys.stdin.readline

query = [0]

while query[-1] != (-1, -1, -1):
    query.append(tuple(map(int, input().split())))

#Dict를 이용한 DP, 구현 문제.
#DP를 이용하면 총 시간 복잡도가 20*20*20*(연산 횟수 최대 4) = 3만2천 정도로 예상이 되는 문제
#전부다 구한다.
#세번째 두번째 첫번째 인덱스 순으로 값을 증가시키면서 조건문 그대로 값을 넣으면 해결된다.
#1. 값을 전부 구한다.
#2. 입력받은 쿼리값을 조건에 맞게 분리해서 처리한다.

tupledict = dict()
tupledict[(0,0,0)] = 1

def inzero(a,b,c):
    return 1 if any(i <= 0 for i in [a,b,c]) else tupledict[(a, b, c)]

def findValue(a,b,c):
    if a < b and b < c:
        return inzero(a, b, c-1) + inzero(a, b-1, c-1) - inzero(a, b-1, c)
    else:
        return inzero(a-1, b, c) + inzero(a-1, b-1, c) + inzero(a-1, b, c-1) - inzero(a-1, b-1, c-1)

for i in range(1, 21):
    for j in range(1, 21):
        for k in range(1, 21):
            tupledict[(i, j, k)] = findValue(i, j, k)

for i in range(1, len(query) - 1):
    if any(j <= 0 for j in query[i]):
        print("w{} = {}".format(query[i], inzero(query[0], query[1], query[2])))
    elif any(j > 20 for j in query[i]):
        print("w{} = {}".format(query[i], tupledict[(20, 20 ,20)]))
    else:
        print("w{} = {}".format(query[i], tupledict[query[i]]))

"""
DP를 Dict를 이용한 구현문제.
1. DP와 재귀를 같이 사용하는 경우가 더 빠르다. --> 필요한 값을 더 효율적으로 찾을 수 있음
2. 값이 더 커진다면
"""