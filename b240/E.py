import sys
from collections import defaultdict as dd
sys.setrecursionlimit(10**7)

N = int(input())
edge = dd(list)
leaf = 1
ans = [0] * N


def dfs(x, last=-1):
    global leaf
    ans[x] = [leaf, leaf]

    for t in edge[x]:
        if t == last:
            continue
        dfs(t, x)
        ans[x][1] = max(ans[x][1], ans[t][1])

    if ans[x][1] == leaf:
        leaf += 1


for _ in range(N-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    edge[v].append(u)
dfs(0)
for i in range(N):
    print(*ans[i])

