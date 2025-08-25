T = int(input(""))

if -273 < T <= 6000:
    if T > 100:
        print("Steam")
    if T < 0:
        print("Ice")
    elif 0 <= T <= 100:
        print("Water")