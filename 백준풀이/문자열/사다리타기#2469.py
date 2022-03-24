import sys
input = sys.stdin.readline

#단순한 구현문제
#1. ?줄이 등장하는 곳을 기준으로 2개의 이동 과정을 구한다.
#2. 첫번째, ?가 등장하기 전까지 등장하는 가로 사다리가 나오면 값을 이동해준다.
#3. ?가 나오면 다시 처음으로 되돌려 index기준으로 1,2를 동일하게 적용한다.
#4. ?이후에 이동한 값의 결과를 가지고 도착순서를 역으로 적용한다.
#5. ?이전의 갑과 이후의 값의 i가 동일하면 *를 집어넣는다.
#5. x방향으로(crt[i] == next[i+1], crt[i+1] == next[i])교환 가능하면 "-*" 넣는다.
#5. 위의 두 경우가 아니면 x를 출력한다.

K = int(input())
N = int(input())
answer = list(input()[:-1])
crt = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:K])
stack = []
for _ in range(N):
    line = input()
    if line[0] == '?':
        stack = crt
        crt = list(range(K))
    for i in range(K - 1):
        if line[i] == '-':
            temp = crt[i]
            crt[i] = crt[i + 1]
            crt[i + 1] = temp

next = [0] * K
for i in range(K):
    next[crt[i]] = answer[i]

print_rtn = []
i = 0
while i < K - 1:
    if stack[i] == next[i]:
        print_rtn.append('*')
        i += 1
        continue
    elif stack[i] == next[i + 1] and stack[i + 1] == next[i]:
        print_rtn.append('-*')
        i += 2
        continue
    else:
        break
rtn = ''.join(print_rtn)[:K - 1]
if len(rtn) == K - 1:
    print(rtn)
else:
    print('x'*(K - 1))