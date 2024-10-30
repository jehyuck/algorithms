def findCount(d, w):
    rtn = 0
    
    prevD = d
    for i in range(len(w)):
        if prevD[w[i]][0] == 1:
            return i + 1
        else:
            prevD = prevD[w[i]]
    return len(w)

def solution(words):
    answer = 0
    d = dict()
    root = dict()
    
    for i in range(len(words)):
        word = words[i]
        if word[0] not in d:
            d[word[0]] = dict()
            d[word[0]][0] = 0
        d[word[0]][0] += 1
        prevDict = d[word[0]]
        crtDict = None
        # print(word)
        for j in range(1, len(word)):
            if word[j] in prevDict:
                crtDict = prevDict[word[j]]
            else:
                crtDict = dict()
                crtDict[0] = 0
                prevDict[word[j]] = crtDict
            # print(crtDict, prevDict, crtDict == prevDict)
            crtDict[0] += 1
            prevDict = crtDict
            
            
    
    # print(d)
    for i in range(len(words)):
        answer += findCount(d, words[i])
              
    return answer