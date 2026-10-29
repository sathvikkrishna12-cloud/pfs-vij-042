#railaway ticket
while True:
    def fare(gen,age):
        rate=1000;
        if(gen=="male"):
            if(age>=60):
                return rate-rate*(50/100)
            else:
                return rate
        elif(gen=="female"):
            if(age>=60):
                return rate-rate*(50/100)
            else:
                return rate-rate*(50/100)
    gen=input("Gender:")
    age=int(input("Enter the pssgr age:"))
    print(f"Ticket fare for passenger is {fare(gen,age)}")

    #or

    while True:
    def price():
        ticket=1000
        gen=input("Enter the gender:")
        age=int(input("Enter the age:"))
        if gen=="m":
            if(age>=60):
                print("Senior Citizen")
                ticket=ticket-(30/100*ticket)
                print(ticket)
            else:
                print("Normal Citizen")
                print(ticket)
        elif gen=="f":
            if(age>=60):
                print("Senior Citizen")
                ticket=ticket-(50/100*ticket)
                print(ticket)
            else:
                print("Normal Citizen")
                ticket=ticket-(30/100*ticket)
                print(ticket)
    price()



