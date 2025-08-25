s, f, l, x = input().split(" ")
s_1 = int(s)
f_1 = int(f)
l_1 = int(l)
x_1 = int(x)

if 1 <= s_1 < f_1 <= 100 and 1 <= l_1 <= min(20, f_1 - s_1) and 1 <= x_1 <= 100:
    if x_1 == f_1 or x_1 > f_1:
        print("exam finished!")
    if x_1 < s_1:
        print("exam did not started!")
    elif x_1 != f_1 and x_1 < f_1 and x_1 > s_1 and x_1 >= ((s_1 + f_1) / 2):
        print(f_1 - x_1)
    elif x_1 < ((s_1 + f_1) / 2) and l_1 != f_1 - s_1:
        print(l_1)
    elif x_1 < ((s_1 + f_1) / 2) and l_1 == f_1 - s_1:
        print(f_1 - x_1)




