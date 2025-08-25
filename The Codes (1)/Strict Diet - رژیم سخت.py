health_indicator = input("")

Red = health_indicator.count("R")
Yellow = health_indicator.count("Y")
Green = health_indicator.count("G")

if Red >= 3:
    print("nakhor lite")
elif Yellow >= 2 and Red >= 2:
    print("nakhor lite")
elif Yellow + Red == 5:
    print("nakhor lite")
else:
    print("rahat baash")

