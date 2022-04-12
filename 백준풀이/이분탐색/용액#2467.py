import sys
input = sys.stdin.readline

answer = []
N = int(input())
sol = tuple(map(int, input().split()))

#이분탐색
#값의 부호와 계산값을 가지고 분할 방향을 정함
#1. 값들에 대해 오름차순으로 반복문을 실행한다.
#2. 두 값의 합이 음수면 오른쪽(last = mid - 1)
#2. 두 값의 합이 양수면 왼쪽으로(start = mid + 1)
ans_value = 2000000001
for i in range(N):
    start = i + 1
    last = N - 1
    while start <= last:
        mid = (start + last) // 2
        temp = sol[i] + sol[mid]
        if ans_value > abs(temp):
            ans_value = abs(temp)
            answer = (i, mid)
        if temp < 0:
            start = mid + 1
        elif temp > 0:
            last = mid - 1
        else:
            break
print(sol[answer[0]], sol[answer[1]])