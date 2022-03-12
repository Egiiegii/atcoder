def solve():
    N, M = map(int, input().split())
    B0 = 0
    A0 = 0
    ans = -(10 ** 20)
    for _ in range(N):
        x, y = map(int, input().split())

        def f(y):
            return (x * y * y + (2 * B0 + x) * y + 2 * A0) // 2

        l = f(1)
        r = f(y)

        pl = 0 if x == 0 else (-2 * B0 - x) // (2 * x)
        pr = 1 + pl
        ans = max(ans, l, r)
        if 1 <= pl <= y:
            ans = max(ans, f(pl))
        if 1 <= pr <= y:
            ans = max(ans, f(pr))

        A0 = f(y)
        B0 += y * x
    print(ans)


T = int(input())
for _ in range(T):
    solve()
