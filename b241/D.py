import sys

from heapq import heappush, heappop, nlargest, nsmallest
sys.setrecursionlimit(10 ** 9 + 1)
Q = int(input())
Qss = []
for _ in range(Q):
    Qss.append(list(map(int, input().split())))

min_5 = []
max_5 = []

for Qs in Qss:
    if Qs[0] == 1:
        try:
            if nsmallest(1, min_5) > Qs[1]:
                heappop(min_5)
                heappush(min_5, Qs[1])
        except Exception:
            heappush(min_5, Qs[1])

        try:
            if nsmallest(1, max_5) > -1 * Qs[1]:
                heappop(max_5)
                heappush(max_5, -1 * Qs[1])
        except Exception:
            heappush(max_5, -1 * Qs[1])
        print(min_5, max_5)
    elif Qs[0] == 2:
        small_k = nsmallest(Qs[2], min_5)
        print(small_k, Qs[1])
        if max(small_k) >= Qs[1]:
            print("-1")
        else:
            print(max(small_k))
    else:
        small_k = nsmallest(Qs[2], max_5)
        if min(small_k) >= -1 * Qs[1]:
            print("-1")
        else:
            print(-1*max(small_k))





