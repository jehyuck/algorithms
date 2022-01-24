#입력
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
blocks = tuple(map(int, input().split()))

# 위로 솟는 꼭지점을 구하고 사이의 차잇값을 구하는 문제
#1. 처음과 끝값은 증가하면 기둥으로 치고, 이외의 값은 양쪽에서 다 증가하면 꼭지점으로 저장한다.
#2. 꼭지점을 순서대로 두개씩 값을 가져온다.
#3. 가장 큰 block을 기준으로 그 다음 큰 값을 하나씩 가져온다.
#3. 가증 큰 block의 인덱스 까지 점점 접근 하면서 사이사이 block차이 값을 answer에 더해준다.
#4. 전부다 계산할 때 까지 반복한다.

up = [1] * W
down = [1] * W

uptemp = 0
downtemp = W - 1

#극점 구하기

#단방향으로 양쪽에서 증가 여부를 구하기
for i in range(1,W):

    if blocks[i] < blocks[uptemp]:
        up[i] = 0
    elif blocks[i] == blocks[uptemp]:
        up[i] = up[uptemp]

    if blocks[-1 - i] < blocks[downtemp]:
        down[-1-i] = 0
    elif blocks[-1 - i] == blocks[downtemp]:
        down[-1-i] = down[downtemp]


    uptemp += 1
    downtemp -= 1

#양쪽에서 증가하는 값인 꼭지점(극점)을 구한다.
edges = []
for i in range(W):
    if all(i == 1 for i in [up[i], down[i]]):
        edges.append((blocks[i], i))
edges.sort()


visited = [False] * W

answer = 0

# 3. 가장 큰 block을 기준으로 그 다음 큰 값을 하나씩 가져온다.
# 3. 가증 큰 block의 인덱스 까지 점점 접근 하면서 사이사이 block차이 값을 answer에 더해준다.
fivot = edges.pop()[1]

while edges:
    value, index = edges.pop()
    for i in range(*sorted([fivot, index])):
        if not visited[i]:
            answer += value - blocks[i] if value > blocks[i] else 0
            visited[i] = True
        else:
            continue
print(answer)

"""
구현문제 양쪽에서 값이 증가하는 값인 극값(꼭지점)을 구하여 사이사이 빗물이 가득찰 때 양을 구하는 문제
1. 꼭지점 들의 사이사이를 가까운 것을 구하려 한점이 실수
--> 큰것을 기준으로 먼저 해줘야지 낭비가 없고 빈칸없이 가득차게 된다. 
"""