x_1, y_1 = input().split(" ")
x_2, y_2 = input().split(" ")
x_3, y_3 = input().split(" ")
X_1 = int(x_1)
Y_1 = int(y_1)
X_2 = int(x_2)
Y_2 = int(y_2)
X_3 = int(x_3)
Y_3 = int(y_3)
a = 0
b = 0
if 0 <= X_1 <= 1000000000 and 0 <= Y_1 <= 1000000000 and 0 <= X_2 <= 1000000000 and 0 <= Y_2 <= 1000000000 and 0 <= X_3 <= 1000000000 and 0 <= Y_3 <= 1000000000:
    if X_1 == X_2:
        a = X_3
    if X_2 == X_3:
        a = X_1
    if X_1 == X_3:
        a = X_2
    if Y_1 == Y_2:
        b = Y_3
    if Y_2 == Y_3:
        b = Y_1
    if Y_1 == Y_3:
        b = Y_2
print(a, b)

