x_1, y_1, x_2, y_2 = input().split(" ")
X_1 = int(x_1)
X_2 = int(x_2)
Y_1 = int(y_1)
Y_2 = int(y_2)

if 1 <= X_1 <= 100 and 1 <= X_2 <= 100 and 1 <= Y_1 <= 100 and 1 <= Y_2 <= 100:
    if Y_1 == Y_2:
        print("Horizontal")
    if X_1 == X_2:
        print("Vertical")
    elif X_1 != X_2 and Y_1 != Y_2:
        print("Try again")