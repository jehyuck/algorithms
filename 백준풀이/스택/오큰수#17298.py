#입력
import sys
input = sys.stdin.readline

N = int(input())


#자료구조 stack 이용한 대소비교 문제
#1. 오른쪽 끝값에서 부터 값을 시작한다.
#2. 스택이 비어있으면 본인을 넣고, dp값은 -1넣고 끝낸다.
#2. 스택이 끝값이 본인보다 크면 그 값을 dp에 넣고 스택에 넣는다.
#2. 스택의 끝값이 지금 값보다 작으면 pop하고 2를 반복
#3. 2의 과정을 dp를 꽉 채울때 까지 반복하낟.


inputlist = tuple(map(int, input().split()))
dp = [-1 for _ in range(N)]
stack = [inputlist[-1]]

for i in range(N-1, -1, -1):
    print(inputlist[i], stack)
    #2. 스택이 비어있으면 본인을 넣고, dp값은 -1넣고 끝낸다.
    while True:
        if stack:
        # 2. 스택이 끝값이 본인보다 크면 그 값을 dp에 넣는다.
            if stack[-1] > inputlist[i]:
                dp[i] = stack[-1]
                stack.append(inputlist[i])
                break
            # 2. 스택의 끝값이 지금 값보다 작으면 pop하고 2를 반복
            else:
                stack.pop()
                continue
        else:
            stack.append(inputlist[i])
            break

print(*dp)

"""
스택을 이용한 대소비교문제
1.처음에 dp를 통해 풀려했다.
--> 그냥 틀린 풀이여서 찾아보고 stack으로 품
"""