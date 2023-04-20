def solution(s):
    answer = 1

    for i in range(len(s) - 1):
        start, end = i, i
        start2, end2 = i, i + 1

        while True:
            if start == -1 or end == len(s):
                answer = max(answer, end - start - 1)
                break
            if s[start] == s[end]:
                start -= 1
                end += 1
            elif s[start] != s[end]:
                answer = max(answer, end - start - 1) 
                break
                
        while True:
            if start2 == -1 or end2 == len(s):
                answer = max(answer, end2 - start2 - 1)
                break
            if s[start2] == s[end2]:
                start2 -= 1
                end2 += 1
            elif s[start2] != s[end2]:
                answer = max(answer, end2 - start2 - 1)
                break
    
    return answer