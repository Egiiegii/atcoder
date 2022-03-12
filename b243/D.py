from collections import deque
N, X = map(int, input().split())
S = input()
stack = deque()

for i in S:
    if i == 'U':
        if len(stack) > 0:
            if stack[-1] in ['L', 'R']:
                stack.pop()
                continue
    stack.append(i)

for s in stack:
    if s == 'U':
        X = X//2
    elif s == 'L':
        X = X * 2
    elif s == 'R':
        X = X * 2 + 1
    else:
        raise Exception()

print(X)
