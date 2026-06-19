a, b, c = map(int, input().split())
if ((a + b + c == 13) or
    (a + b - c == 13) or
    (a - b + c == 13) or
    (-a + b + c == 13)):
    print("Yes")
else:
    print("No")
