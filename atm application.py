while True:
    bal=100000
    card="bcsns"
    password=142
    a=input("Insert the card ")
    if(a==card):
        print("Welcome Chaitanya")
        b=int(input("Enter the password:"))
        if(b==password):
            print("Authentication Successful")
            opt=int(input("Options are 1.Balance Enquiry \n \t  2.Withdraw "))
            if(opt==1):
                print("Account Balance:",bal)
            elif(opt==2):
                wd=int(input("Enter the amount:"))
                if(wd>bal):
                    print("Insufficient Funds")
                else:
                    print("Please collect the cash")
                    bal=bal-wd
                    print("Remaining Balance:",bal)
                    print("Thank You and Please visit again!")
            else:
                print("Invalid option")
        else:
            print("Invalid or Incorrect Password")
    else:
        print("Invalid Credentials")
