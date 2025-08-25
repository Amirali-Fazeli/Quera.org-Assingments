X = int(input(""))
N = int(input(""))

if 0 <= X <= 20 and 0 <= N <= 100:
    if N == 0:
        print(20)
    if N == 7:
        print(X)
    elif 1 <= N <= 6 or N > 7:
        X = X - N
        if X < 0:
            print(0)
        else:
            print(X)

