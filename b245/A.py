import datetime
import sys
A, B, C, D =map(int, input().split())

if A == 0 and B == 0 and C == 23 and D == 59:
    print("Takahashi")
    sys.exit(0)

x1 = datetime.datetime(year=2000,month=1, day= 1, minute=A, second=B)
x2 = datetime.datetime(year=2000,month=1, day= 1, minute=C, second=D)
x2 = x2 + datetime.timedelta(seconds=1)
if x1 >= x2:
    print("Aoki")
else:
    print("Takahashi")
