def Phone_Number(number):
    for i in number:
        if number.count(i) >= 4:
            return True
    for i in range(len(number) - 2):
        if number[i] == number[i + 1] == number[i + 2]:
            return True
    if number == number[::-1]:
        return True

    return False

t = int(input())
outcome = []
for j in range(t):
    phone_num = input()
    if Phone_Number(phone_num):
        outcome.append(("Ronde!"))
    else:
        outcome.append("Rond Nist")
for out_come in outcome:
    print(out_come)


