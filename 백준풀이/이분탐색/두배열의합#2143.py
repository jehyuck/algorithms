import sys
input = sys.stdin.readline

T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

#누적합, 이진탐색
#1. 누적합을 구한다.
#2. 부분합을 dict를 이용해 구한다.
#3. 경우의 수의 곱을 이용해 두배열의 합을 구한다.


def prefix(arr, n):
    for i in range(1, n):
        arr[i] += arr[i - 1]


def subfix(arr, n):
    rtn = {}
    arr = [0] + arr
    for i in range(n + 1):
        for j in range(i):
            t = arr[i] - arr[j]
            if t in rtn:
                rtn[arr[i] - arr[j]] += 1
            else:
                rtn[t] = 1
    return rtn


prefix(A, N)
prefix(B, M)
sub_A = subfix(A, N)
sub_B = subfix(B, M)

answer = 0
for key in sub_A:
    t = T - key
    if t in sub_B:
        answer += sub_B[T - key] * sub_A[key]

print(answer)