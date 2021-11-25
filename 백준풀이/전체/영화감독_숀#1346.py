#입력받기
n = int(input())

count = 1
k = 666

while count != n:
    k += 1
    if '666' in str(k):
        count += 1

print(k)