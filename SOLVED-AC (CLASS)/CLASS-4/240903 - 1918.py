# 후위 표기식
# 골드 2

from collections import deque

infix = input()

op_stack = deque()

operators = ['+', '-', '*', '/', '(', ')']

for i in range(len(infix)):
    if infix[i] not in operators:
        print(infix[i], end='')
        continue

    if infix[i] == '(':
        op_stack.appendleft(infix[i])
    elif infix[i] == ')':
        tmp = op_stack.popleft()
        while tmp != '(':
            print(tmp, end='')
            tmp = op_stack.popleft()
    elif infix[i] == '*':

