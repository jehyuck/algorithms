#입력 최적화
import sys
input = sys.stdin.readline

#입력
N = int(input())

#dp를 이용한 풀이, 최대와 최소를 분리해서 푼다.
#1. 첫 줄을 입력받고 그값으 최대와 최소의 그릇을 복사해서 선언
#2. 다음 줄을 입력(a,b,c) 받는다
#2-1. 이전줄에서 인접한값(ex:a의 경우 1,2, c의경우:2,3가 인덱스)을 고르고
#     최대의 경우 이중 최댓값 최소의 경우 이중 최솟값을 고른다
#2-2. 각각 두개씩 존재하는 abc 값을 그릇의 새 값으로 설정한다.
#2-3. 입력이 끝날때 까지 반복한다.


min_list = list(map(int,input().split()))
max_list = min_list.copy()

for i in range(1,N):
    a, b, c = map(int,input().split())

    min1, min3 = min(min_list[:2]), min(min_list[1:])
    min2 = min(min1, min3)

    max1, max3 = max(max_list[:2]), max(max_list[1:])
    max2 = max(max1, max3)

    max_list = [a+max1, b+max2, c+max3]
    min_list = [a+min1, b+min2, c+min3]

print(max(max_list), min(min_list))