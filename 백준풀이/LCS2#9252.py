#입력
a_Word = list(input())
b_Word = list(input())

#lcs를 dp를 이용해서 푼다.
alen = len(a_Word)
blen = len(b_Word)

dp = [['' for _ in range(blen+1)] for _ in range(alen+1)]
#같으면 길이 추가 and, 문자열추가
#다르면 길이 이어받기, 문자열 이어받기
for i in range(1,alen+1):

    for j in range(1,blen+1):
        #같을 시 길이를 대각선 위의 것으로 추가한다.
        if a_Word[i-1] == b_Word[j-1]:
            dp[i][j] = dp[i-1][j-1] + a_Word[i-1]
        else:
            #문제 조건에서 아무거나 출력하라 하였기 때문에
            #등호의 종류는 >, >= 상관없음
            if len(dp[i][j-1]) > len(dp[i-1][j]):
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = dp[i-1][j]
#출력
print(len(dp[-1][-1]),dp[-1][-1],sep="\n")

"""
DP를 이용한 LCS를 구하는 문제
1.기준 문자열과 비교 문자열을 설정한다.(나의 경우: b=기준, a=비교)
2.dp를 a길이+1, b길이+1로 초기값=0 으로 선언한다. 
3.a를 하나하나 b에 비교를한다.(for a길이{for b길이})
4.같으면 dp[b][a] = dp[b-1][a-1]+같은단어
5.다르면 dp[b][a] = (a-1, b-1 위치의 값중 더 큰 것

수정한 것
처음엔 문자열과 길이를 두가지 다 구했다
1.문자열만 구하고 출력을 (len(문자열), 문자열)으로하면 된다.
--> dp의 요소를 [count,word] ==>[word]  
"""
