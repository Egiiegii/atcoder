import sys

V, A, B, C = map(int, input().split())

while True:
    V -= A
    if V < 0:
        print("F")
        sys.exit(0)
    V -= B
    if V < 0:
        print("M")
        sys.exit(0)
    V -= C
    if V < 0:
        print("T")
        sys.exit(0)
