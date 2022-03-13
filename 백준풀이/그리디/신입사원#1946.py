import sys
input = sys.stdin.readline

#그리디
#1. 입력을 받는다
#2. (a, b)에 대해 a에 대해 정렬된 순서로 b값을 갖는 list를 만든다.
#3. a로 정렬된 순서로 나열된 b_list에 대해 0 - n 순서로 순회한다.
#4. 순회하면서 최솟값이 바뀔 때마다 answer += 1한다.
#5. 출력

T = int(input())

for i in range(T):
    N = int(input())
    rank_list = [0] * (N + 1)
    for j in range(N):
        a, b = map(int, input().split())
        rank_list[a] = b

    m = N + 1
    answer = 0
    for j in range(1, N + 1):
        if m > rank_list[j]:
            m = rank_list[j]
            answer += 1

    print(answer)