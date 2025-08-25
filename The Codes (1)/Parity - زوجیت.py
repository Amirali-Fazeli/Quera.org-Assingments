n = int(input(""))
if 1 <= n <= 50:
    if n == 1:
        print("fard")
    if n == 2:
        print("fard")
    elif n % 2 == 0:
        print("fard")
    elif n == 3 or n == 5 or n == 7 or n == 11 or n == 13 or n == 17 or n == 19 or n == 23 or n == 29 or n == 31 or n == 37 or n == 41 or n == 43 or n == 47:
        print("zoj")
    elif n % 2 != 0 and n != 1:
        print("fard")
