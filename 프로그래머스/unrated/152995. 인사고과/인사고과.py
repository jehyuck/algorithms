from collections import deque as d

def solution(scores):
    answer = -1
    target = scores[0].copy()
    
    que = d(sorted(scores, reverse=True))
    prev = que[0]
    max_prev = [0, 0]
    temp = d()
    while que:
        crt = que.popleft()
        
        if prev[0] > crt[0]:
            if max_prev[1] < prev[1]:
                max_prev = prev
            prev = crt
        if max_prev[1] > crt[1]:
            continue
        else:
            temp.append(crt)
    
    result = sorted(temp, key = lambda x: -sum(x))
    for i in range(len(result)):
        if target[0] == result[i][0] and target[1] == result[i][1]:
            answer = i + 1
            break
    return answer