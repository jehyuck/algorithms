#입력
N, K = int(input()), int(input())

#이진탐색을 이용한 K값 찾기
#1.N을 통해 최댓값과 최솟값을 구한다.
#2.mid를 최댓값과 최솟값합//2==몫 으로 정한다.
#2-1. mid값 이하인 수들의 갯수를 구한다.
#2-2. 갯수가 k와 작으면 최솟값을 mid +1로 한다.
#2-3. 갯수가 k보다 크거나 같으면 최댓값을 mid-1로 하고 answer를 mid로 한다.
#2-4. 최솟값이 최댓값보다 크거나 같아질 때 까지반복
#3. 최댓값이나 최솟값중 한개를 출력하고 마무리

#1
left = 1
right = min(N*N,10**9)
answer = right
#2-(1--4)
while left <= right:
    #2
    mid = (left + right)//2
    # print(left, right, mid)
    #2-1
    count = 0
    for i in range(1, N+1):
        count += min(N, mid//i)
        if count > K:
            break
    # print(count, K)
    #2-(2--4)
    if count >= K:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
print(answer)

"""
이진탐색을 이용한 갯수 새기 문제
1.처음에 기본 이진탐색으로 했다가 최솟값을 구하는 이진탐색으로함.
-->k와 count가 같을때, k가 클때, count가 클 때로 분리했었음
-->count가 >= k로 합쳐줌 
    k가 count랑 같은 경우 반복문을 나가게 된다면
    존재하지 않는 값에서 반복문을 나갈 수가 있음
    백준 문제 페이지 기준 1번 예제에서 6,7,8의 카운트가 동일
    6일 때만 정답이여야 함
    
"""