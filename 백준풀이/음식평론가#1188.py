#입력
n, m = map(int,input().split())

#유클리드 호재법
#최소공배수
def lcm(a, b):
    #최대공약수
    def gcd(a, b):
        while b != 0:
            temp = b
            b = a%b
            a = temp
        return a

    return (a * b)/gcd(a,b)

cut_max = lcm(n, m)
cut_nsize = cut_max//n
cut_msize = cut_max//m

cut_n = [cut_nsize]*n
cut_m = [cut_msize]*m

cut_count = 0

for i in range(m):
    #사람에게 소세지를 채워넣어준다.
    while cut_m[i] > 0:
        #소세지를 한개 뽑아
        sausage = cut_n.pop()

        #그 소세지와 사람이 가져야 할 양에 따라
        #1. 사람이 크거나 같으면 그냥 넣는다.
        #2. 소세지가 더 크면 소세지를 잘라 사람에게 주고
        # count += 1 소세지를 다시 소세지 통에 넣어준다.
        if sausage <= cut_m[i]:
            cut_m[i] -= sausage
        else:
            sausage -= cut_m[i]
            cut_m[i] = 0
            cut_n.append(sausage)
            cut_count += 1

print(cut_count)


"""
다른풀이 생각해보기
사람의 수에서- 최대 공약수
M - GCD(N, M)
"""