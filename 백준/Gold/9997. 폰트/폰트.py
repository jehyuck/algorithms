from itertools import combinations as c
N = int(input())

def stringtobit(s):
    rtn = 0
    for i in s:
        rtn |= 1 << (ord(i) - ord('a'))
    return rtn


words = [stringtobit(input()) for _ in range(N)]
target = (1 << 26) - 1
# print(words, target)
answer = 0

for i in range(1, N + 1):
    for j in c(words, i):
        temp = 0
        for k in j:
            # print(k)
            temp |= k
        # print(temp)
        if temp == target:
            answer += 1

print(answer)
