N = int(input())
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))

same_cnt = 0
diff_cnt = 0

for i_A, A in enumerate(As):
    for i_B, B in enumerate(Bs):
        if A == B:
            if i_A == i_B:
                same_cnt += 1
            else:
                diff_cnt += 1
            break
print(same_cnt)
print(diff_cnt)
