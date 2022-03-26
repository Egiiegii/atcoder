from collections import defaultdict as dd
import sys
N = input()
As = list(map(int, input().split()))

d = dd(int)

for A in As:
    d[A]=1


for i in range(2001):
    if d[i] == 0:
        print(i)
        sys.exit(0)
