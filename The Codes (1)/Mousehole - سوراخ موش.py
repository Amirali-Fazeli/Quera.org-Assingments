x_1, x_2 = input().split(" ")
X_1 = int(x_1)
X_2 = int(x_2)

if 0 <= X_1 <= 2 and 0 <= X_2 <= 2:
    if X_2 - X_1 == 2:
        print("RR")
    if X_2 - X_1 == 1:
        print("R")
    if X_1 - X_2 == 2:
        print("LL")
    if X_1 - X_2 == 1:
        print("L")
    elif X_1 == X_2:
        print("Saal Noo Mobarak!")
