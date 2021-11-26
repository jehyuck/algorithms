
#입력
n = int(input())


#스택을 담는 그릇과 함수
class Mystack:
    def __init__(self):
        self.stack = []

    def push(self,x):
        self.stack.append(x)

    def empty(self):
        if len(self.stack) == 0:
            return 1
        else:
            return 0

    def pop(self):
        if self.empty():
            return -1
        else:
            return self.stack.pop()

    def size(self):
        return len(self.stack)

    def top(self):
        if self.empty():
            return -1
        else:
            return self.stack[-1]

#스택 초기화
stack = Mystack()
execute = []

#명령어를 받는다
for i in range(n):
    execute.append(input().split(' '))

#실행문과 실행을 한다
for a in execute:
    if a[0] == "push":
        stack.push(a[1])
    elif a[0] == "pop":
        print(stack.pop())
    elif a[0] == "size":
        print(stack.size())
    elif a[0] == "empty":
        print(stack.empty())
    elif a[0] == "top":
        print(stack.top())

