cnt = 0
for i in range(111, 1000):
    a = i % 10
    b = i // 10 % 10
    c = i // 100 % 10
    if abs(a -b) <=1 and abs (b-c)<=1:
        cnt += 1
        print(i)
print(cnt)
