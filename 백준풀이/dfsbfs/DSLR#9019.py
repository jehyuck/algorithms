import sys
from collections import deque as d
input = sys.stdin.readline

#bfs
#1. 답이 나올 때 까지 모든 수에 대해 4가지 연산을 실행한다.
#2. D: 2를 곱하고 10000으로 나눈 나머지
#2. S: 1을 뺀다. -1일때 예외처리
#2. L: 10000으로 나눈 몫과 나머지 * 10의 합
#2. R: 10으로 나눈 나머지와 10으로 나눈 몫과 나머지 * 1000의 합
#3. 각 연산들을 방문하지 않은 곳들을 queue에 저장하고 방문하면 pass한다.
#4. 정답에 도달 했을 때의 경로를 출력한다.

T = int(input())
answer = []
for _ in range(T):
    visit = [1] * 10000
    start, target = map(int, input().split())
    que = d()
    que.append((start, ""))
    visit[start] = 0
    n, s = (start, "")

    while n != target:
        print(que)
        temp = (n * 2) % 10000
        if visit[temp]:
            visit[temp] = 0
            que.append((temp, s + 'D'))
        temp = n - 1 if n else 9999
        if visit[temp]:
            visit[temp] = 0
            que.append((temp, s + 'S'))
        a, b = divmod(n, 1000)
        temp = a + b * 10
        if visit[temp]:
            visit[temp] = 0
            que.append((temp, s + 'L'))
        a, b = divmod(n, 10)
        temp = a + b * 1000
        if visit[temp]:
            visit[temp] = 0
            que.append((temp, s + 'R'))
        n, s = que.popleft()
    answer.append(s)

print(*answer, sep="\n")