#입력
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = tuple(map(int,input().split()))
sums = [0]
for i in range(N):
    sums.append((sums[i] + nums[i])%M)

#누적 합을 이용한 전체 탐색 문제
#1. 누적합을 구할때 미리 값을 M으로 나눠 저장한다.
#2. 누적합 list의 요소에 대해서 등장한 숫자들을 counting한다.
#3. 등장한 숫자들을 counting 하고 갯수n[i]에 대해 1부터 (n[i]-1)의 합을 구한다.
#4. 3번 과정중의 모든 합을 구한다.

counting_dict = dict()
#2. 누적합 list의 요소에 대해서 등장한 숫자들을 counting한다.
for i in range(1, N + 1):
    if sums[i] not in counting_dict:
        counting_dict[sums[i]] = 1
    else:
        counting_dict[sums[i]] += 1

#3. 등장한 숫자들을 counting 하고 갯수n[i]에 대해 1부터 (n[i]-1)의 합을 구한다.
answer = 0
for i in counting_dict:
    count = counting_dict[i]
    if count == 1:
        continue
    else:
        answer += ((count-1)*count)//2

print(answer + counting_dict[0] if 0 in counting_dict else 0)

"""
누적합과 값 카운팅 문제
1.전부다 탐색하려면 10**12의 시간이걸림
2.전부다 계산하려면 10**9의 값들이 많이 생김

값을 줄이기 위해 누적합에 미리 M의 값을 나눠 저장
나머지 값이 같은 것 끼리만 누적합 차가 0이 된다는 점을 이용
반복 횟수를 줄이기 위해 O(N)인 누적합 list를 순회해 값 카운팅함(메모리도 최대 10**3의 자연수 갯수)
반복횟수를 줄이기 위해 합 공식을 이용해 값을 구함 ex(3개일때 (3)(3-1)//2) 그리고 0의 갯수 만큼 답에 더해줌
"""