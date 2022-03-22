import sys
from collections import deque as d
input = sys.stdin.readline

#문자열
#1. 문자열을 순회한다.
#2. 3부분으로 나눠 문제를 푼다.
#2. 폭발 문자열이 들어오면 temp에 쌓는다.
#2. 폭발 문자열이 조건에 맞게 된다면 폭발 시킨다.
#2. 폭발 문자열이 쌓이는 도중 첫번째 폭발 값이 들어오면 진행중인 문자열 stack에 넣음
#2. 폭발 문자열이 쌓이는 도중 폭발문자열이 아니거나  아닌 값이 들어오면 left로 넘긴다.
#2. 모든 문자열 검증이 끝나면 반복문을 종료한다.
#3. stack과 center부분에 남은게 있다면 left로 처리한다.

str_ = list(input())[:-1]
target = list(input())[:-1]
left = []
center = []
right = d(str_)
stack = []
crt = 0

while right:
    temp = right.popleft()

    if len(center) == len(target):
        right.appendleft(temp)
        center = stack.pop() if stack else []
        continue

    if temp not in target:
        for i in range(len(stack)):
            left.extend(stack[i])
        left.extend(center)
        left.append(temp)
        stack = []
        center = []
        continue

    if temp != target[len(center)]:
        if temp == target[0]:
            stack.append(center)
            center = []
            right.appendleft(temp)
        else:
            for i in range(len(stack)):
                left.extend(stack[i])
            left.extend(center)
            left.append(temp)
            center = []
            stack = []
    else:
        center.append(temp)

if stack:
    for i in range(len(stack)):
        left.extend(stack[i])
    stack = []
    left.extend(center)
    if center != target:
        center = []
if center != target:
    left.extend(center)
print(''.join(left if left else ['FRULA']))
