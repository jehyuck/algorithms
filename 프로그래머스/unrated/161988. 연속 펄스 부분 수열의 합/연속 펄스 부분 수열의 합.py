def solution(sequence):
    answer = 0
    n = len(sequence)
    prefix = [0] * (n + 1)
    
    value_min = 0
    value_max = 0
    for i in range(n):
        if i % 2 == 0:
            prefix[i + 1] = prefix[i] + sequence[i]
        else:
            prefix[i + 1] = prefix[i] - sequence[i]
        value_min = min(value_min, prefix[i + 1])
        value_max = max(value_max, prefix[i + 1])
        
    # print(abs(value_min - value_max))
    return abs(value_min - value_max)