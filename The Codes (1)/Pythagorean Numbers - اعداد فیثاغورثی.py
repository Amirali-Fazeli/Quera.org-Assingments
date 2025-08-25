a = int(input(""))
b = int(input(""))
c = int(input(""))

if 1 <= a <= 150 and 1 <= b <= 150 and 1 <= c <= 150:
    if a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == a ** 2 + b ** 2:
        print("YES")
    else:
        print("NO")
