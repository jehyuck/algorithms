#입력
N, M = map(int, input().split())

maxcommon = 1
for i in range(1, min(N, M) + 1):
    if N%i == 0 and M%i == 0:
        maxcommon = i

print(maxcommon)
print((M//maxcommon) * N)

"""
기본적인 반복문을 이용한 최대공약수 최소공배수문제
1. 유클리드 호제법을 공부해서 다시구해보자
"""