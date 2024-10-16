
passs = " ="
nums = set(map(str, range(2, 10)))

def split(s):
    global passs, nums
    
    rtn = []
    idx = 0
    ele = ""
    mins = 1
    while idx < len (s):
        if s[idx] in passs:
            if ele:
                rtn.append(ele)
                ele = ""
            idx += 1
            continue
        if s[idx] in nums:
            mins = max(mins, int(s[idx]))
        ele += s[idx]
        idx += 1
    rtn.append(ele)
    return rtn, mins

def getDto(ex):
    rtn = []
    mins = 1
    for i in ex:
        ele, tempMins = split(i)
        mins = max(mins, tempMins)
        rtn.append(ele)
        
    return rtn, mins


def ten2z(a, z):
    if a == 0:
        return "0"
    rtn = ""
    # print(a, z)
    while a:
        # print(a % 2, a // 2,rtn)
        rtn += str(a % z)
        a //= z
    return rtn[::-1] 


def z210(a, z):
    if a == 0:
        return int(a)
    rtn = 0
    idx = 0
    
    while idx < len(a):
        rtn += int(a[idx]) * (z ** (len(a) - idx - 1))
        idx += 1

    return rtn


def calc(ex, z):
    a, e, b, r = ex
    
    a10 = z210(a, z)
    b10 = z210(b, z)
    r10 = a10 - b10 if e == "-" else a10 + b10
    return str(ten2z(r10, z))


def calc_zin(ex, zin):
    remove = set()
    z_iter = iter(zin)
    # print(zin)
    for _ in range(len(zin)):
        z = z_iter.__next__()
        # print(ex, z)
        pos = calc(ex, z)
        # print(z, pos, ex[3])
        if pos != ex[3]:
            remove.add(z)
    # print(zin, remove , zin - remove)
    return zin - remove

def getAnswer(q, z):
    answer = True
    z_iter = iter(z)
    for _ in range(len(z)):
        z = z_iter.__next__()
        value = calc(q, z)
        if answer == True:
            answer = value
        elif answer != value:
            return "?"
    return answer
       
    
def join(ex):
    formatstr= "{} {} {} = {}"
    return formatstr.format(*ex)
    
    
def solution(expressions):
    answer = []
    ex = expressions
    
    exLi, s = getDto(ex)
    l = 9
    zins = set(range(s + 1, l + 1))
    # print(zins, s)
    q = []
    for i in range(len(exLi)):
        if exLi[i][-1] == "X":
            q.append(exLi[i])
        else:
            zins = calc_zin(exLi[i], zins)
    
    for i in range(len(q)):
        value = getAnswer(q[i], zins)
        q[i][3] = value
        answer.append(join(q[i]))
    # print(q, zins)
    return answer