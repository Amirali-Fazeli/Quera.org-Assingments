n = int(input(""))
m = float(input(""))

BMI = float(n / (m ** 2))
BMI_1 = format(BMI, ".2f")
print(BMI_1)

if 1 <= n <= 200 and 1 <= m <= 10:
    if BMI < 18.5:
        print("Underweight")
    if 18.5 <= BMI < 25:
        print("Normal")
    if 25 <= BMI < 30:
        print("Overweight")
    if 30 <= BMI:
        print("Obese")