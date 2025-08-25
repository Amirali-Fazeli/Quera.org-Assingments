n = int(input())
lstt = input().split()
lst = [int(number) for number in lstt]

chap = 0
rast = n - 1

while chap < rast:
    vasat = chap + (rast - chap) // 3
    vasat_1 = rast - (rast - chap) // 3

    if lst[vasat] < lst[vasat_1]:
        chap = vasat + 1
    else:
        rast = vasat_1 - 1

outcome = lst[chap]
print(outcome)


