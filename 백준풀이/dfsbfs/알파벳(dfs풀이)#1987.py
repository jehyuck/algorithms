#입력
import sys
input = sys.stdin.readline

R, C = map(int, input().split())

maps = []
# letters = set()
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for _ in range(R):
    maps.append(tuple(map(lambda x:ord(x)-65, input().rstrip())))


#dfs를 이용한 전체탐색
#1. 4방향중 갈수 있는 방향(방문하지 않았고, 알파벳이 겹치지 않는) 방향을 반복문을 통해 들어간다.
#2. 들어가면 방문처리하고 알파벳경로 등록하고 answer와 len(set)중 더 큰 값을 answer에 저장
#3. answer == len(letters)이면 조기에 종료한다.

def dfs(y,x, ans):
    global answer
    answer = max(answer, ans)
    # print(y,x)
    for i in direction:
        my = i[0] + y
        mx = i[1] + x
        if 0 <= my < R and 0 <= mx < C and visited[maps[my][mx]] == 0:

            visited[maps[my][mx]] = 1
            dfs(my,mx, ans + 1)
            visited[maps[my][mx]] = 0


answer = 1
visited = [0] * 26
visited[maps[0][0]] = 1
dfs(0,0, answer)
print(answer)