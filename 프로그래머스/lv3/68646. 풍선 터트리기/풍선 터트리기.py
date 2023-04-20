def solution(a):
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