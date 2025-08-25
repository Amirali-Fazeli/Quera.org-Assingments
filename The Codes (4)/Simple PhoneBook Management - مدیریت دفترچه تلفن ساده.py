Contacts = []

while True:
    print("Phonebook")
    print("No. 1 ---> Add Contact")
    print("No. 2 ---> Show Contact List")
    print("No. 3 ---> Show by Name")
    print("No. 4 ---> The End")

    Selection = input("Select Your Number: ")
    if Selection == "1":
        Name = input("What is the Name of the Contact: ")
        Phone_Number = input("Enter the Number: ")
        E_mail = input("Enter the E_mail Address: ")
        Address = input("What is the Address of the Contact: ")

        if len(Phone_Number) != 11 or not Phone_Number.startswith("0"):
            print("Invalid Phone_Number")
            continue
        Contact = {"Name": Name, "Phone_Number": Phone_Number, "E_mail": E_mail, "Address": Address}
        Contacts.append(Contact)
        print("The Contact Has Been Added Successfully")

    elif Selection == "2":
        if not Contacts:
            print("The Phonebook is Empty")
        else:
            for Contact in Contacts:
                print("Name:", Contact["Name"])
                print("Phone_Number:", Contact["Phone_Number"])
                print("E_mail:", Contact["E_mail"])
                print("Address:", Contact["Address"])
                print()

    elif Selection == "3":
        Name = input("What is the Name of the Contact: ")
        find = False
        for Contact in Contacts:
            if Contact["Name"] == Name:
                print("Name:", Contact["Name"])
                print("Phone_Number:", Contact["Phone_Number"])
                print("E_mail:", Contact["E_mail"])
                print("Address:", Contact["Address"])
                print()
                find = True
                break
        if not find:
            print("No Contact Has Been found")

    elif Selection == "4":
        break
    else:
        print("Please Select Again")
    print()