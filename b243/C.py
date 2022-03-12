import sys
from collections import Counter, defaultdict as dd

N = int(input())
xs = dd(list)
ys = []
xys = []
for _ in range(N):
    xy = list(map(int, input().split()))
    xys.append(xy)

S = input()
for idx, xy in enumerate(xys):
    ys.append(xy[1])
    if S[idx] == 'L':
        t = 1
    else:
        t = -1
    xs[xy[1]].append((xy[0], t))
# print("input")
# print(xy)
# print(xs)
ys_counter = Counter(ys)
ys_commons = ys_counter.most_common()
# print(ys_commons)
for ys_common in ys_commons:
    if ys_common[1] < 2:
        continue

    lr_list = xs[ys_common[0]]
    # print(lr_list)

    a = sorted(lr_list, key=lambda x: (x[1], x[0]))
    # print(ys_common[0], a)
    if a[0][0] < a[-1][0] and a[0][1] != a[-1][1]:
        print("Yes")
        sys.exit(0)
print("No")
