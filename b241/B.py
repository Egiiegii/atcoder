import sys
N, M =map(int, input().split())
As =list(map(int, input().split()))
Bs =list(map(int, input().split()))

for B in Bs:
    try:
        As.remove(B)

    except Exception:
        print("No")
        sys.exit(0)
print("Yes")

