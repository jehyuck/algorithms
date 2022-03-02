target = int(input())

two_five = [0,0]
n = 1
##수학문제
#1. 1부터 n까지 모든 수를 본다.
#2. 모든 수 하나하나에 2와 5로 나눠지지 않을 때까지 count 한다.
#3. 두개 수 중 작은 수를 선택한다.
#(5만 count 해도 됨)
while n <= target:
    m = n
    while m % 2 == 0:
        two_five[0] += 1
        m /= 2
    m = n
    while m % 5 == 0:
        two_five[1] += 1
        m /= 5
    n += 1

print(min(two_five))
