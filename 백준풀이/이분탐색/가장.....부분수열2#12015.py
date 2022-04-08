import sys
input = sys.stdin.readline

#dp에 이진탐색을 적용
#1. 값이 dp값과 작거나 같으면 last = mid - 1
#2. 값이 dp값보다 크면 first = mid + 1
#3. 이 방법으로 dp값보다 작은 가장 큰 값을 구한다.
#4. 해당인덱스에 값을 추가하거나 변경해준다.
N = int(input())
seq = tuple(map(int, input().split()))
A = []
c = -1
for i in range(N):
    first = 0
    last = c
    while first <= last:
        mid = (first + last) // 2
        # print(i, first, last, mid, A, seq[i])
        if seq[i] > A[mid]:
            first = mid + 1
        else:
            last = mid - 1
    # print(last)
    if c == last:
        A.append(seq[i])
        c += 1
    else:
        A[last + 1] = seq[i]

print(c + 1)

#파이썬으로 풀리지 않음
#좀 더 효율적인 방법 찾아보기
#ex) 값이 초과하는 경우 이분탐색 하지 않고 바로 값 추가하기