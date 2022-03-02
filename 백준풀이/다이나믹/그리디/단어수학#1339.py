#입력

N = int(input())



#그리디를 이용해 값을 할당
#1. 알파뱃들의 자릿수 합을 구한다.(ABCA의 경우 A= 1001, B= 100, C= 10)
#2. 큰 수부터 등장할수 있는 수들을 대입해 가장 큰 값을 할당한다.
#   위의 예시에선(9,8,7) 9를 대입시 A가 9009로 가장크니 A에 9를 할당
#3. 모든 알파벳이 할당 될 때까지 이를 반복한다.
nums = []
letterdict = dict()
for i in range(N):

    letters = input()
    for j in range(len(letters)):

        if not letters[j] in letterdict:
            letterdict[letters[j]] = 10**(len(letters) - j-1)
        else:
            letterdict[letters[j]] += 10**(len(letters) - j-1)

votelist = list(range(9,9-len(letterdict.keys()),-1))
answer = 0

for i in votelist:
    maxvalue = max(map(lambda x: [i*letterdict[x], x], letterdict.keys()))
    answer += maxvalue[0]
    letterdict.pop(maxvalue[1])

print(answer)

"""
그리디를 이용한 문제
1. 처음에 시간복잡도가 넘을것을 알면서도 풀었다.
-->10P10 * 100 * a --> 최소 4억가까이 된다.
-->다른 방법을 찾았어야 함 =그리디
"""