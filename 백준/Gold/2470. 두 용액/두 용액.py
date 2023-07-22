
def solution():
    N = int(input())

    liquor = list(map(int, input().split()))
    liquor.sort()
    left = 0
    right = len(liquor) - 1

    answer = [left, right]
    answer_value = 1000000000 * 2 + 1
    while left < right:
        crt_value = liquor[left] + liquor[right]

        if abs(crt_value) < abs(answer_value):
            answer_value = crt_value
            answer[0] = left
            answer[1] = right

        if crt_value == 0:
            break
        elif crt_value < 0:
            left += 1
        elif crt_value > 0:
            right -= 1

    return [liquor[answer[0]], liquor[answer[1]]]


print(*solution())
