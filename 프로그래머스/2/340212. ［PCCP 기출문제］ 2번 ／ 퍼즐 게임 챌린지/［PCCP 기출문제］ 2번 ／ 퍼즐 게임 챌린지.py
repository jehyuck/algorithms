def sol_puzzle(prevtime, diff, time, l):
    n = (diff - l if diff > l else 0)
    rtn = time + (n * (time + prevtime) if n > 0 else 0)
    return rtn
    
    

def sol_puzzles(diffs, times, limit, level):
    rtn = 0
    for i in range(len(diffs)):
        diff = diffs[i]
        time = times[i]
        prevtime = (times[i - 1] if i > 0 else 0)
        rtn += sol_puzzle(prevtime, diff, time, level)
    return rtn



def solution(diffs, times, limit):
    answer = 0
    maxLevel = max(diffs)
    minLevel = 1
    s = minLevel
    l = maxLevel
    opt = maxLevel
    while s <= l:
        answer = (s + l) // 2
        
        value = sol_puzzles(diffs, times, limit, answer)
        if value > limit:
            s = answer + 1
        elif value < limit:
            opt = min(opt, answer)
            l = answer - 1
        else:
            opt = answer
            break
        
    return opt