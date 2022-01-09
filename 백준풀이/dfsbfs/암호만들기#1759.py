#큐사용하기
from collections import deque as d

#알파벳가져오기
import string
gather = set("aeiou")

#입력
L, C = map(int, input().split())
letters = sorted(list(input().split()))

#bfs를 이용한 전체탐색
#1. 모든 문자에 대해 사전순으로 bfs를 한다.
#2. 길이가 L이 될때까지 갯수를 추가하면서 queue에 넣는다.
#3. L만큼의 길이로 채워지면 자음수 모음수를 체크한다.
#3-1. 조건에 맞는경우 printlist에 추가한다.
leftqueue = d([[i] for i in range(C)])
printlist = []

while leftqueue:
    crt = leftqueue.popleft()

    # 3. L만큼의 길이로 채워지면 자음수 모음수를 체크한다.
    if len(crt) == L:
        print(crt)
        # 3-1. 조건에 맞는경우 printlist에 추가한다.
        con_count = 0
        get_count = 0

        for i in crt:
            if letters[i] in gather:
                get_count += 1
            else:
                con_count += 1
        if get_count >= 1 and con_count >= 2:
            printlist.append("".join(list(map(lambda x:letters[x],crt))))
    else:
        # 2. 길이가 L이 될때까지 갯수를 추가하면서 queue에 넣는다.
        temp = []
        for i in range(crt[-1]+1, C):
            leftqueue.append(crt+[i])


print(*printlist, sep="\n")

"""
bfs를 이용한 전체탐색
1. 백트래킹을 생각하다가 입력범위가 적어 전체탐색을함
--> 15C7이 최대 경우의수 약 6000
"""