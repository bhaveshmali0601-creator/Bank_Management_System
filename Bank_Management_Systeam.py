accounts = {}

while True:
    print("\n===== Bank Management System =====")
    print("1. Create Account")
    print("2. View Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Check Balance")
    print("6. Delete Account")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        acc_no = input("Enter Account Number: ")
        name = input("Enter Name: ")
        balance = float(input("Enter Initial Balance: "))

        accounts[acc_no] = {"name": name, "balance": balance}
        print("Account Created Successfully!")

    elif choice == "2":
        acc_no = input("Enter Account Number: ")
        if acc_no in accounts:
            print("Name:", accounts[acc_no]["name"])
            print("Balance:", accounts[acc_no]["balance"])
        else:
            print("Account Not Found!")

    elif choice == "3":
        acc_no = input("Enter Account Number: ")
        amount = float(input("Enter Amount: "))
        if acc_no in accounts:
            accounts[acc_no]["balance"] += amount
            print("Deposit Successful!")
        else:
            print("Account Not Found!")

    elif choice == "4":
        acc_no = input("Enter Account Number: ")
        amount = float(input("Enter Amount: "))
        if acc_no in accounts:
            if accounts[acc_no]["balance"] >= amount:
                accounts[acc_no]["balance"] -= amount
                print("Withdrawal Successful!")
            else:
                print("Insufficient Balance!")
        else:
            print("Account Not Found!")

    elif choice == "5":
        acc_no = input("Enter Account Number: ")
        if acc_no in accounts:
            print("Balance:", accounts[acc_no]["balance"])
        else:
            print("Account Not Found!")

    elif choice == "6":
        acc_no = input("Enter Account Number: ")
        if acc_no in accounts:
            del accounts[acc_no]
            print("Account Deleted!")
        else:
            print("Account Not Found!")

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
