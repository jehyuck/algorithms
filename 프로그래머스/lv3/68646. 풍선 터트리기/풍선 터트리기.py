def solution(a):
    answer = 0

    dp_left = [0] * len(a)
    dp_right = [0] * len(a)

    dp_left[0] = a[0]
    dp_right[-1] = a[-1]

    for i in range(1, len(a)):
        dp_left[i] = a[i]
        if dp_left[i] > dp_left[i - 1]:
            dp_left[i] = dp_left[i - 1]

    for i in range(len(a) - 2, -1, -1):
        dp_right[i] = a[i]
        if dp_right[i] > dp_right[i + 1]:
            dp_right[i] = dp_right[i + 1]

    for i in range(len(a)):
        if a[i] == dp_left[i] or a[i] == dp_right[i]:
            answer += 1

    return answer


def solution1(a):
    answer = set()
    N = len(a)
    n = N - 1
    
    answer.add(0)
    answer.add(n)
    left_max = a[0]
    right_max = a[-1]
    for i in range(N):
        if left_max > a[i]:
            answer.add(i)
            left_max = a[i]
        if right_max > a[n - i]:
            answer.add(n - i)
            right_max = a[n - i]
    
    return len(answer)