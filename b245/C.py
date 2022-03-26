import sys
N, K = map(int, input().split())
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))

now = [As[0], Bs[0]]
for i in range(1, N):
    new = []
    for z in [As[i], Bs[i]]:
        for j in now:
            if abs(z - j) <= K:
                new.append(z)
                break
    if not new:
        print("No")
        sys.exit(0)
    now = new
print("Yes")
