from collections import deque as dd


def getTime(i):
    a, b = map(int, i.split(":"))
    return a * 60 + b


def init(plans):
    rtn = []
    for i in plans:
        p = [i[0], getTime(i[1]), int(i[2])]
        rtn.append(p)
    rtn.sort(key = lambda x: x[1])
    return dd(rtn)


def solve(p):
    rtn = []
    
    stack = dd()
    s = p.popleft()
    time = s[1]
    while p:
        finish = s[1] + s[2]
        n, stime, pl = p[0]
        print(s, p[0])
        if finish > stime:
            s[2] -= stime - s[1]
            stack.append(s)
            s = p.popleft()
        elif finish == stime:
            rtn.append(s[0])
            s = p.popleft()
        else:
            rtn.append(s[0])
            if stack:
                s = stack.pop()
                s[1] = finish
            else:
                s = p.popleft()
    stack.append(s)
    while stack:
        rtn.append(stack.pop()[0])
    
    return rtn
    

def solution(plans):
    answer = []
    plans = init(plans)
    answer = solve(plans)
    return answer