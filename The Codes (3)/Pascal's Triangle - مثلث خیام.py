n = int(input())
m = 1
if 1 <= n <= 10:
    for i in range(n):
        for j in range(1, m - i + 1):
            print("", end = "")
        for j in range(i + 1):
            if (j == 0 or i == 0):
                m = 1
            else:
                m = m * (i - j + 1) // j
            print(m, end = " ")
        print()
