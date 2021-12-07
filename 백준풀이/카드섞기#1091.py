#입력
n = int(input())
cards = [i for i in range(n)]
cards_set = [set(), set(), set()]

#입력2,3
p = list(map(int,input().split()))
s = list(map(int,input().split()))

#원하는 카드 배치
for i in range(n):
    cards_set[p[i]].add(i)


#카드의 싸이클을 찾는 함수
visited = [False] * n

def find_cycle(f):
    cy = [f]
    crt = s[f]

    #본인이 나올때까지 계속 이어지는 값을 append
    while crt != f:
        visited[crt] = True
        cy.append(crt)
        crt = s[crt]

    return cy

#최소공배수 함수
def lcm(li):
    #최대공약수를 활용
    def gdc(a,b):
        while b > 0:
            temp = b
            b = a % b
            a = temp
        return a
    while len(li) != 1:
        a = li.pop()
        b = li.pop()

        li.append((a*b) / gdc(a,b))
    return li

#답과 확인하기
def confirm():
    for i in range(n):
        if cards[i] in cards_set[i%3]:
            continue
        else:
            return False
    return True

#셔플
def do_cycle():
    rtn = [0]*n
    for i in range(n):
        rtn[s[i]] = cards[i]

    return rtn

#모든 방향에 대해 싸이클을 찾는다.
#싸이클에 존재하지 않는것만 찾는다
cycle_list = []
for i in range(n):
    if not visited[i]:
        visited[i] = True
        cycle_list.append(find_cycle(i))

#cards셔플에 존재하는 cycle들의 최소공배수가
#전체의 싸이클이다.
max_count = int(lcm([len(i) for i in cycle_list])[0])

#모든 원상으로 돌아갈때까지 count를 잰다.
count = 0
for i in range(max_count):
    if confirm():
        break
    else:
        cards = do_cycle()
        count += 1

#원상으로 돌아가는 사이클을 돌아도 찾아내지 못했다면 -1출력
if count == max_count:
    print(-1)
else:
    print(count)

