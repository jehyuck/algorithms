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
    que.append((start, 1))
    visit[start] = 1
    n, s = que.popleft()

    while n != target:
        temp = (n * 2) % 10000
        if visit[temp]:
            visit[temp] = 0
            que.append((temp, s * 4 + 0))
        temp = n - 1 if n else 9999
        if visit[temp]:
            visit[temp] = 0
            que.append((temp, s * 4 + 1))
        a, b = divmod(n, 1000)
        temp = a + b * 10
        if visit[temp]:
            visit[temp] = 0
            que.append((temp, s * 4 + 2))
        a, b = divmod(n, 10)
        temp = a + b * 1000
        if visit[temp]:
            visit[temp] = 0
            que.append((temp, s * 4 + 3))
        n, s = que.popleft()
    answer.append(s)

order = ("DSLR")
def print_recur(num):
    if num == 1:
        return
    d, m = divmod(num, 4)
    print_recur(d)
    print(order[m], end="")


for i in answer:
    print_recur(i)
    print()


"""
시간을 줄이기 위해
1. que속의 list --> tuple
2. tuple을 언패킹해 모든 값들을 그 값으로 치환
3. DSLR루트를 기록하기 위해 사용한 문자열 연산을 전부 제거
(str) + (str) -> 'DSLR' + 'D' >{계속 문자열이 copy됨}
 ㄴ->>형식을 아래의 형식으로
 n * 4 + (0,1,2,3 중 택 1) (비트마스킹?? 형식)
출력시 재귀 형식으로 끝에 나머지 부터 출력
"""