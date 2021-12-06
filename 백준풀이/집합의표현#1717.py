#입력 최적화
import sys
sys.setrecursionlimit(10**5)
#입력
n, r = map(int,sys.stdin.readline().split())


parents = [i for i in range(n+1)]

#유니온 파인드 함수
def union(a,b):
    a = press(a)
    b = press(b)

    if a > b:
        parents[a] = b
    else:
        parents[b] = a

def press(a):
    if parents[a] == a:
        return a

    p = press(parents[a])
    parents[a] = p
    return p


#입력2

for i in range(r):
    o, a, b = map(int,sys.stdin.readline().split())
    if o == 0:
        union(a,b)

    else:
        if press(a) == press(b):
            print("YES")
        else:
            print("NO")
