#입력 최적화
import sys
input = sys.stdin.readline
allN = sum([2**i for i in range(20)])
#입력
m = int(input())
S = 0

def add(S, n):
    S = S | 2**(n-1)
    return S

def remove(S, n):
    S = S & ~2**(n-1)
    return S

def check(S, n):
    bins = bin(S)
    if n > len(bins)-2:
        print(0)
    else:
        print(bins[-n])


def toggle(S, n):
    S = S ^ 2**(n-1)
    return S

for i in range(m):
    ex = input().split()

    if ex[0] == 'all':
        S = allN
    elif ex[0] == 'empty':
        S = 0
    elif ex[0] == 'add':
        S = add(S, int(ex[1]))
    elif ex[0] == 'remove':
        S = remove(S, int(ex[1]))
    elif ex[0] == 'check':
        check(S, int(ex[1]))
    elif ex[0] == 'toggle':
        S = toggle(S, int(ex[1]))

"""
비트마스크에 대한 이해하고 또 풀어보기
"""