#입력
input_list = list(map(int, input().split()))
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
N, prob = input_list[0], list(map(lambda x: x*0.01,input_list[1:]))

#dfs 백트래킹을 이용한 총합 구하기
#1. 스택에서 위치를 뽑는다
#2. 경로 배열이 크기가 N이되면 답에 확률값을 더해주고 끝낸다.
#3. 4방향에 대해 경로, 이동위치, 확률을 구한다.
#4. 이동위치가 경로속에 존재하지 않고, 확률이 0인 방향을 제외하고 stack에 넣어준다.
#5. 모든곳을 탐색 할 때 까지이 더해준다.

#1. 스택에서 위치를 뽑는다
def dfs(y, x, crtprob, f):
    global answer

    # 2. 경로 배열이 크기가 N이되면 답에 확률값을 더해주고 끝낸다.
    if f == N:
        answer += crtprob
        return
    if crtprob == 0:
        return

    # 3. 4방향에 대해 경로, 이동위치, 확률을 구한다.
    for i in range(4):
        my, mx = directions[i][0] + y, directions[i][1] + x

        # 4. 이동위치가 경로속에 존재하지 않고, 확률이 0인 방향을 제외하고 stack에 넣어준다.
        if visit[my][mx]:
            continue
        else:
            visit[my][mx] = True
            dfs(my, mx, crtprob * prob[i], f + 1)
            visit[my][mx] = False
answer = 0
visit = [[False for _ in range(N*2 + 1)] for _ in range(N*2 + 1)]
visit[N][N] = True

dfs(N, N, 1, 0)
print(float(answer))

"""
#bfs 백트래킹을이용한 전체탐색문제
1.처음에 set을 이용해 경로를 일일히 저장하는 식으로 품
--> 매 스택 과정에 set을(최대 길이가 14) 생성하기 때문에 과정이 길어질수록 메모리와 시간을 차지함
--> 재귀의 스택과정과 map행렬을 이용해 O(1)인 경로작성을 구성
    dfs(이동경로)로 들어갈때 방문처리 해당과정이 끝나고 함수의 stackpop이 이루어질때 방문하지 않았다고 재처리
"""