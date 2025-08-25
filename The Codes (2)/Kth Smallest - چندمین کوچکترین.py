input_number = input()
n, k = input_number.split()
n = int(n)
k = int(k)
input_lst = input()
lstt = input_lst.split()
lst = []

if 1 <= k <= n <= 100:

    for number in lstt:
        lst.append(int(number))

    while True:
        a = lst[0]
        chap = []
        rast = []
        for number in lst[1:]:
            if number < a:
                chap.append(number)
            else:
                rast.append(number)
        if len(chap) == k - 1:
            outcome = a
            break
        elif len(chap) >= k:
            lst = chap
        else:
            lst = rast
            k = k - (len(chap) + 1)

    print(outcome)

