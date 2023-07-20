from collections import deque as d

def split(s):
    calc = {'+', '-'}

    num_li = d()
    temp = d()
    for i in s:
        if i in calc:
            num_li.append(int(''.join(temp)))
            num_li.append(i)
            temp = []
        else:
            temp.append(i)
    num_li.append(int(''.join(temp)))
    return num_li

def solution():
    expr = input()

    num_li  = split(expr)
    first = 0
    ex = ''
    last = 0

    only_minus = d()
    while len(num_li) > 1:
        first = num_li.popleft()
        ex = num_li.popleft()
        last = num_li.popleft()


        if ex == '+':
            num_li.appendleft(first + last)
        else:
            only_minus.append(first)
            num_li.appendleft(last)
    answer = 0
    if not only_minus:
        return num_li[0]
    else:
        answer = only_minus[0]
        for i in range(1, len(only_minus)):
            answer -= only_minus[i]
        answer-= num_li[0]

    return answer

print(solution())