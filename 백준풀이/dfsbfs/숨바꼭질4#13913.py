from collections import deque as d
#입력
n, k = map(int,input().split())

#형의 값을 기준으로 동생에게 다가간다.bfs 사용
#1. 3가지경우(1을 뺌, 1을 더함, 2를 곱함)를 방문한다.
#2. 방문했을 경우 방문하지 않는다
#3. 방문하지 않았을 경우 key=본인: value=이전 값으로 dict요소를 초기화한다.

#큐와 형의 족적을 남기는 변수 초기화
queue = d([n])

#첫번째 list 요소는 어디 위치에서 왔는지 2번째 요소는 움직인 횟수가 저장된다
move = {n:[n,0]}

#기본으로 큐가 비어지게 되면 탈출
while queue:

    #가장 왼쪽의 것을 뽑아온다.
    crt = queue.popleft()

    #그게 동생의 위치면 탈출
    if crt == k:
        break
    else:
        #아니면 알고리즘을 시작한다.

        #아니면 3가지 방법 방문
        preque = [crt-1,crt+1,crt*2]

        #방문할 곳에 동생의 위치가 존재한다면 형의 족적을 남기고
        #movecount += 1을 해준다.
        if k in preque:
            move[k] = [crt,move[crt][1]+1]
            break

        #방문하지 않은곳만을 큐에 넣는다
        #조건: 0보다 크고 방문하지 않은곳
        for i in preque:
            if i not in move and i>=0 and i <= 200000:
                #현재위치와 움직인 횟수를 i위치에 저장하고 큐에 등록
                move[i] = [crt,move[crt][1]+1]
                queue.append(i)

print_move = [k]
crt = k

#현재까지 움직인 공간을 역추적해서 print 해야하는 footprint를 저장한다.
while crt!=n:
    print_move.append(move[crt][0])
    crt = move[crt][0]

#걸린 횟수를 출력하고
#역추적한 footprint이므로 reverse해준다
print(move[k][1])
print(*reversed(print_move))

"""
bfs를 이용해 가장 빠른 경로를 탐색하는 문제
풀기위해 한 노력
1.그리디한 방법에서 bfs로 방법을 변경
-->조건에 따라 값을 더하거나 빼주려다가 모든경우를 고려해야한단 생각이 들어 방법을 바꿈
2.없는 조건을 만들어 푸는 실수를 하여 문제를 다시 읽음
-->처음에 값을 2로 나누는 경우를 고려하고 풀었다.

"""