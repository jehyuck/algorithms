#입력
n = int(input())

#변수 선언 map과 방문여부
maps = []
unvisited = [[True for _ in range(n)]for _ in range(n)]
for i in range(n):
    maps.append(list(input()))

#방향(상하좌우) 설정
direction = [(1,0), (0,1), (-1,0), (0,-1)]
#dfs 정의
cnt = 0
def dfs(p):
    global cnt
    cnt += 1

    for i in direction:
        dx, dy = i
        x, y = p[1] + dy, p[0] + dx
        if x < n and y < n and x >= 0 and y >= 0 and maps[y][x] == '1' and unvisited[y][x]:
            unvisited[y][x] = False
            dfs([y,x])
#dfs 실행
answer = []

for i in range(n):
    for j in range(n):
        if unvisited[i][j] and maps[i][j] == '1':
            cnt = 0
            unvisited[i][j] = False
            dfs([i,j])
            answer.append(cnt)

#출력
print(len(answer))
for i in sorted(answer):
    print(i)