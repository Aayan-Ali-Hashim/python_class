# we will take input from user ,the pin.
# if pin is correct we will take age as input from user 
acc_balance = "$2000"
pin = input("Please enter your pin\n")
if pin == "1234":
    age = int(input("Enter your age\n"))
    if age >= 25 and age<=100:
        print("Access Allowed")
        print("1.Withdraw\n2.Deposit\n3.Account Balance")
        input_value = int(input("Enter the number of your desired option\n"))
        if input_value==1:
           withdraw_amount = int(input("Enter the amount\n"))
           print(f"You have withdrawn ${withdraw_amount} from your account , thanks for using Bee Bank")
        elif input_value==2:
            deposit_value = int(input("Enter the amount you want to deposit\n"))
            print("Insert the cash in the slot")
            print("Thank you for using Bee Bank")
        elif input_value==3:
            print("Your account balance is" + " " + acc_balance)
            print("Thank you for using Bee Bank")
        else:
            print("Enter correct value")
    elif age<25:
        print("You are below 25")
    else:
        print("Input correct value")

else:
    print("Wrong pin entered")