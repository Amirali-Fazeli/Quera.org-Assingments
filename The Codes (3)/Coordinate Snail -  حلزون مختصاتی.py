n = int(input())
a = 0
b = 0
jahat = 0
rast, bala, chap, paeen = 0, 1, 2, 3
har_harekat = 1
harekat = 0


while harekat < n - 1:
    if jahat == rast:
        a = a + har_harekat
    elif jahat == bala:
        b = b + har_harekat
    elif jahat == chap:
        a = a - har_harekat
    elif jahat == paeen:
        b = b - har_harekat

    harekat = harekat + 1

    if harekat % 2 == 0:
        har_harekat = har_harekat + 1

    jahat = (jahat + 1) % 4

print(a, b)


