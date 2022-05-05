import sys
input = sys.stdin.readline

N = int(input())
seq = tuple(map(int, input().split()))
A = [seq[0]]
idx = [0] * len(seq)
c = 0

#이진탐색, dp 두번
#1. LIS 상태를 저장할 dp와 idx를 저장할 dp를 구한다.
#2. dp처음에 입력값 0번째를 넣는다.
#3. 모든 입력값에 대해 순서대로 LIS판별을 한다.
#4-1. dp 끝값이 seq[i]보다 작으면 바로 넣는다.
#4-2. dp 끝값이 seq[i]보다 크면 이진 탐색을 통해 올바른 위치를 구한다.
#4-2. 아니면 idx[i] = seq[i]의 dp상의 인덱스 를 기록한다.
#5. crt = len(dp)로 값을 두고 crt를 dp 처럼 이용한다.
#5-1. len(idx) - 0으로 1씩 줄어드는 반복문을 실행한다.
#5-2. crt == idx[i]이면 answer[idx[i]] = seq[i] 하고 crt를 1 빼준다.
#6. answer를 출력한다.

for i in range(1, N):
    first = 0
    last = c
    if A[-1] < seq[i]:
        A.append(seq[i])
        c += 1
    else:
        while first <= last:
            mid = (first + last) // 2
            if seq[i] > A[mid]:
                first = mid + 1
            else:
                last = mid - 1
        A[last + 1] = seq[i]
    idx[i] = last + 1
len_A = len(A)
ans = [0] * len_A
crt = len_A - 1

for i in range(len(seq) - 1, -1, -1):
    if idx[i] == crt:
        ans[crt] = seq[i]
        crt -= 1
        if crt == -1:
            break

print(len(ans))
print(*ans)


"""
최적화를 하기 위해 idx를 따로 저장하고, reverse함수를 쓰지 않고 ans를 미리 만들었고
seq를 튜플로 만들었다.
쓸데없는 이진탐색을 하지 않기 위해서 dp끝값을 먼저 탐색하고 조건에 맞는 상황에 dp를 실행헀다
"""