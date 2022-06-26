import sys

input = sys.stdin.readline
N = int(input())
ele = [int(input()) for _ in range(N)]
stack = [(0, 0)]
crt = 1
ans = 0
while stack and crt < N:
    if ele[stack[-1][0]] < ele[crt]:
        ans += stack.pop()[1]
        if not stack:
            stack.append((crt, 0))
            crt += 1
        ans += 1
    elif ele[stack[-1][0]] == ele[crt]:
        stack.append((crt, stack[-1][1] + 1))
        crt += 1
    else:
        stack.append((crt, 1))
        crt += 1
for i in stack:
    ans += i[1]
print(ans)