import sys

input = sys.stdin.readline
def solution():
    answer = 0

    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    for i in range(N):
        left = 1 if i == 0 else 0
        right = N - 2 if i == N - 1 else N - 1

        while left < right:
            sum_two = nums[left] + nums[right]

            if sum_two > nums[i]:
                right -= 1 if right - 1 != i else 2
            elif sum_two < nums[i]:
                left += 1 if left + 1 != i else 2
            else:
                answer += 1
                break

    return answer

print(solution())