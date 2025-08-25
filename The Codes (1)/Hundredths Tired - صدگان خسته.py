num = int(input(""))
Num = int(input(""))

reverse_num = str(num)[::-1]
reverse_Num = str(Num)[::-1]
Reverse_num = int(reverse_num)
Reverse_Num = int(reverse_Num)

if num > 0 and Num > 0:
    if Reverse_Num > Reverse_num:
        print(num, "<", Num)
    if Reverse_Num < Reverse_num:
        print(Num, "<", num)
    if Reverse_Num == Reverse_num:
        print(Num, "=", num)

