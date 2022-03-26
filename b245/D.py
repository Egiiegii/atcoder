import sys
N, M = map(int, input().split())
As = list(map(int, input().split()))
Cs = list(map(int, input().split()))

Bs = []
while As[0]==0:
    As.pop(0)
    Cs.pop(0)
len_a = len(As)

Bs.append(int(Cs[0]/As[0]))

for i in range(1, M+1):
    B = Cs[i]
    # print(B)
    for idx_a in range(i, 0, -1):
        idx_b = i - idx_a
        # print("idx_a, idx_b", idx_a, idx_b)
        if idx_a >= len_a:
            continue
        B -= As[idx_a]*Bs[idx_b]
        # print(B)
    # print("last", B)
    Bs.append(int(B/As[0]))
print(" ".join(map(str, Bs)))
