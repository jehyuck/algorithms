import sys
input = sys.stdin.readline

N, M, s = int(input()), int(input()), input()

#문자열 전체탐색
#1. ioi가 연속되는 문자열 갯수를 찾는 문제
#2. ioi가 연속되면 1을 더해준다.
#2. ioi가 연속되지 않는다면 subset에 넣고 다시 ioi를 찾는다.
#3. subset을 가지고 NIOI이 나올 수 있는 갯수의 총합을 구한다.
start = 0
max_make = 0
crt = 0

subset = []
while crt < M:
    if start == 0 and s[crt] == 'I':
        start = 1
        crt += 1
    elif start == 1 and s[crt : crt + 2] == "OI":
        max_make += 1
        crt += 2
    elif start == 1 and s[crt : crt + 2] != "OI":
        if max_make >= N:
            subset.append(max_make)
        max_make = 0
        start = 0
    else:
        crt += 1

answer = 0
for i in subset:
    answer += i - N + 1

print(answer)
