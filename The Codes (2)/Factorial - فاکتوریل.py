n = int(input())
factor = 1
m = 1

if 0 <= n <= 10000:
    while m <= n:
        factor = factor * m
        m = m + 1
    print(factor)