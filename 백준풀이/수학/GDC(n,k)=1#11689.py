import sys
input = sys.stdin.readline
N = int(input())
def sosu(N):
    d = 2  # 나누는 수
    limit = N ** 0.5 + 2
    answer = N
    while N != 1 and d < limit:
        if N % d != 0:
            d += 1
        else:
            while N % d == 0:
                N //= d
            answer -= answer // d
    if N > 1:
        answer -= answer // N
    return answer
print(sosu(N))
# def sosu(N):
#     d = 2  # 나누는 수
#     limit = N ** 0.5 + 2
#     soinsu = {}
#     while N != 1 and d < limit:
#         if N % d != 0:
#             d += 1
#         else:
#             N //= d
#             if d in soinsu:
#                 soinsu[d] += 1
#             else:
#                 soinsu[d] = 1
#     if d > limit:
#         soinsu[N] = 1
#     return soinsu
#
# soinsu = sosu(N)
# answer = 1
# for i in soinsu.keys():
#     answer *= (i - 1) * (i ** (soinsu[i] - 1))
# print(answer)


"""
오일러 피? 공식을 이용한 빠르게 소인수를 찾는 문제
모르면 아예 못푸는 문제 남의 코드 많이 참조함
"""