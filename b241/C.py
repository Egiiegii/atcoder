import sys

sys.setrecursionlimit(10 ** 9 + 1)
N = int(input())
S = []
for i in range(N):
    S.append(input().rstrip())


def check_list(ls):
    count = 0
    for l in ls:
        if l == '.':
            count += 1
    if count <= 2:
        print("Yes")
        sys.exit(0)


for i in range(N):
    for j in range(N):
        if i + 6 <= N:
            # check left
            ls = [
                S[i][j],
                S[i + 1][j],
                S[i + 2][j],
                S[i + 3][j],
                S[i + 4][j],
                S[i + 5][j]
            ]
            check_list(ls)

        if j + 6 <= N:
            # check bottom
            ls = S[i][j:j + 6]
            check_list(ls)
        if i + 6 <= N and j + 6 <= N:
            # check diagonal
            ls = [
                S[i][j],
                S[i + 1][j + 1],
                S[i + 2][j + 2],
                S[i + 3][j + 3],
                S[i + 4][j + 4],
                S[i + 5][j + 5]
            ]
            check_list(ls)
        # check diagonal
        if i + 6 <= N and j - 6 <= 0:
            ls = [
                S[i][j],
                S[i + 1][j - 1],
                S[i + 2][j - 2],
                S[i + 3][j - 3],
                S[i + 4][j - 4],
                S[i + 5][j - 5]
            ]
            check_list(ls)
print("No")
