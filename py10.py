#Function -- a function is a block of reuseful code of that is used to perform
   ##a single or multiple tasks.
#python gives multiple functions like print and you can make your own functions
   ##and these are called user defined functions
#function blocks begin with the keyword 'def' followed by the function
   ##name and parantheses()

'''a=10
b=20
print("The sum is",a+b)
print("The diff is",a-b)
print("The product is",a*b)
a=100
b=200
print("The sum is",a+b)
print("The diff is",a-b)
print("The product is",a*b)
a=1000
b=2000
print("The sum is",a+b)
print("The diff is",a-b)
print("The product is",a*b)'''


#functions
'''def calculate(a,b):
    print("The sum is",a+b)
    print("The diff is",a-b)
    print("The product is",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''

# **,%,//
'''def calculate(a,b):
    print("The pow is",pow(a,b))
    print("The mod is",a%b)
    print("The int div is",a//b)
calculate(2,4)
calculate(4,2)
calculate(10,5)'''

'''def add(a,b):
    c=a+b
    print(c)
add(2,4)'''

#run-time

'''def add():
    a=int(input())
    b=int(input())
    print(a+b)
add()'''

'''def fullname():
    a=input("Enter first name:")
    b=input("Enter last name:")
    print((a+" "+b).title())
fullname()'''

#print() just shows the human user output in a console.
#return()--it is used to terminate the function and gives back a value
         ## from the function.

# print v/s return

'''def sub(a,b):
    print(a-b)
sub(4,10)'''

'''def sub(a,b):
    return (a-b)
print(sub(4,10))'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(2,4)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return(c)
    #return d
    #return e
    return c,d,e
print(cal(2,4))'''

#tasks

'''def cal():
    a=int(input("value of a:"))
    b=int(input("value of b:"))
    opt=int(input("Options are 1.Add\n\t\t2.Sub\n\t\t3.Mul:"))
    if(opt==1):
        print("The sum is",a+b)
    elif(opt==2):
        print("The subtraction is",a-b)
    elif(opt==3):
        print("The product is",a*b)
    else:
        print("Invalid option")
cal()'''

'''def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
a=int(input("value of a:"))
b=int(input("value of b:"))
opt=int(input("Options are 1.Add\n\t\t2.Sub\n\t\t3.Mul:"))
if(opt==1):
    print("The sum is",add(a,b))
elif(opt==2):
    print("The subtraction is",sub(a,b))
elif(opt==3):
    print("The product is",mul(a,b))
else:
    print("Invalid option")'''

'''def add():
    print("The sum is",a+b)
def sub():
    print("The subtraction is",a-b)
def mul():
    print("The product is",a*b)
while True:
    a=int(input("value of a:"))
    b=int(input("value of b:"))
    opt=int(input("Options are 1.Add\n\t\t2.Sub\n\t\t3.Mul:"))
    if(opt==1):
        add()
    elif(opt==2):
        sub()
    elif(opt==3):
        mul()
    else:
        print("Invalid option")'''

#keyword and positional arguments

'''def details(id,name,mailid):
    id=10
    name="chaitu"
    mailid="ch@gmail.com"
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")'''

'''def details(id,name,mailid):
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")
details(id=20,name="ramu",mailid="ramu@gmail.com")
details(id=30,name="ram",mailid="ram@gmail.com")
details(40,"raj","raj@gmail.com")
details("rajiv","rajiv@gmail.com",50)
details(name="uday",mailid="uday@gmail.com",id=60)'''

#task

'''def emp(id,name,mailid,desig):
    print(id,name,mailid,desig)
emp(id="id",name="name",mailid="mailid",desig="desig")
emp(10,"rama","rama@gmail.com","manager")
emp(20,"raj","raj@gmail.com","asst manager")
emp(30,"ram","ram@gmail.com","resource manager")
emp(40,"rajiv","rajiv@gmail.com","personal assistant")
emp(10,"ramu","ramu@gmail.com","finance")'''

#Default arguments

'''def grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery("rice",2000)'''

'''def grocery(item="sugar",price=100):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery()'''

'''def grocery(item,price=200):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery("dhal")'''

'''def grocery(item="ghee",price):
    #non-def arg follows def arg
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery(500)'''

'''def grocery(item,price,qty=1):
    print("item is %s" %item)
    print("price is %.2f" %price)
    print("qty is %d" %qty)
grocery("salt",30)'''

#task

'''def bakery(cake,price,qty=1):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("qty is %d" %qty)
bakery("red velevt",2500)'''

#Split bill

'''def split_bill(bill,t):
    return bill/t
bill=float(input("Enter total bill amount:"))
t=int(input("Enter total members in group:"))
print("The amount for each member is =%.1f" %split_bill(bill,t))
print(f"The amount per person is {split_bill(bill,t)}")'''

'''def splitbill():
    a=int(input("Enter the total members:"))
    b=int(input("Enter the total amount:"))
    print("per head bill is",b//a) #formatting/string formatting
splitbill()'''

'''def splitbill():
    a=int(input("Enter the total members:"))
    b=int(input("Enter the total amount:"))
    c=b//a
    print(f"per head bill is {c}") #f-string
    print("per head bill is {}".format(c)) #format method
splitbill()'''

#star arguments.

# * arguments -> * is used to unpack the elements.

'''a=[3,4,5,6,7,8,9]
print(a)
print(*a)'''

'''a=(3,4,5,6,7,8,9)
print(a)
print(*a)'''

'''a={3,4,5,6,7,8,9}
print(a)
print(*a)'''

'''a={"month":10,"year":2026}
print(a)
print(a.values())
print(*a)
print(*a.values())'''

'''a,b,c=3,4,5,6,7,8,9,10,11
print(a)
print(b)   #Error
print(c)'''

'''a,b,c=3,4,5
print(a)
print(b)
print(c)'''

'''a,b,*c=3,4,5,6,7,8,9,10,11
print(a)
print(b)
print(*c)'''

'''a='codegnan'
print(a)
print(*a)'''

'''a,b,c='codegnan'
print(a)
print(b)   #Error
print(c)'''

'''a,b,c='cod'
print(a)
print(b)   
print(c)'''

'''*a,b,c='codegnan'
print(*a)
print(b)
print(c)'''

#variable length arguments -> variable length arguments are automatically stored
## in tuples and we use star arguments. 

'''def check(*a):
    print(a)
    print(type(a))
check()
b=[2,3,4,5,6,7,8]
check(*b)
c=(5,6,7,8)
check(*c)
d={5,6,7,8,10}
check(*d)
e={"city":"vja"}
check(*c)'''

'''def check1(*a):
    d=2
    print(a)
    print(type(a))
    for i in a:
        d=d+i
        print(d)
check1()
check1(2,3,4,5,6)
check1(2,3,4.2,5.3)
check1(1,2,3,5,2.3,4.2,"chaitanya")'''

'''def check1(*a):
    d=2
    print(a)
    print(type(a))
    for i in a:
        if(type(i) in (int,float)):    #or if(type(i) is not str):
            d=d+i
        print(d)
check1()
check1(2,3,4,5,6)
check1(2,3,4.2,5.3)
check1(1,2,3,5,2.3,4.2,"chaitanya")'''

#Railway Ticket
'''while True:
    def fare(gen,age):
        rate=1000;
        if(gen=="male"):
            if(age>=60):
                return rate-rate*(30/100)
            else:
                return rate
        elif(gen=="female"):
            if(age>=60):
                return rate-rate*(50/100)
            else:
                return rate-rate*(30/100)
    gen=input("Gender:")
    age=int(input("Enter the pssgr age:"))
    print(f"Ticket fare for passenger is {fare(gen,age)}")'''

'''while True:
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
    price()'''

#kwargs(**)

'''def check(**a):
    print(a)
    print(type(a))
check()
details={'idnos':[10,20,30],
         'names':["prasad","venkat","ajay"],
         "status":["p","a","p"]}
check(**details)'''

'''def check(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
check()
details={'idnos':[10,20,30],
         'names':["prasad","venkat","ajay"],
         "status":["p","a","p"]}
check(**details)'''

# both * AND ** usage.

'''def check(*a,**b):
    d=2
    print(a)
    print(type(a))
    for i in a:
        if(type(i) in (int,float)):
            d=d+i
        print(d)
    print(b)
    print(type(b))
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
check()
a=(10,20,30,40,50,55.4,60.2)
details={'idnos':[10,20,30],
         'names':["prasad","venkat","ajay"],
         "status":["p","a","p"]}
check(*a,**details)'''

#ASCII
#chr()
'''print(chr(90))
print(chr(65))
print(chr(91))'''

#ord()
'''print(ord("a"))
print(ord("z"))'''

'''print(ord(90))  #error
print(chr("a")) #error'''

#task

'''for i in range(ord("A"),ord("Z")+1):   #or range(65,91)
    print({chr(i)},end=" ")
for i in range(ord("a"),ord("z")+1):   #or range(96,123)
    print(chr(i),end=" ")'''

'''a=input("Enter the name:")
for i in a:
    print(f"{i}={ord(i)}",end=" ")'''

##pattrns

#right-angle triangle pattern
'''a=int(input("Enter a number:"))
for i in range(a):
    for j in range(i+1):
        print("*",end=" ")
    print()'''

#reverse right-angle triangle pattern
'''a=int(input("Enter a number:"))
for i in range(a):
    for j in range(a-i):
        print("*",end=" ")
    print()'''

#square pattern
'''a=int(input("Enter a number:"))
for i in range(a):
    for j in range(a):
        print("*",end=" ")
    print()'''

#equilateral triangle
'''a=int(input("Enter a number:"))
for i in range(1,a+1):
    print(" "*(a-i)+"* "*i)'''

#Global and Local variables
#A variable is inside and outside the function is called as global and local variables.
#A variable is defined above the function and is accessible to the entire global space
 ##is called a global variable and the variable declared inside the function is called
 ##local variable.

#first acse og global variable

'''a=4
def check():
    print("inside value is",a)
check()
print("outside value is",a)'''

#second case of global variable

'''a=2
def check2():
    a=5
    a**=2
    print("inside value is",a)
check2()
print("outside value is",a)'''

#third case of both global and local variables

'''a=3
b=6
def check3():
    a=4
    print("inside value is",a)
    a=5
    print("updated value is",a+5)
    b=12 #local variable if not initialized outside the function
    b+=a
    print("value of b is",b)
check3()
print("a value is",a)
print("b value is",b)'''

#Usage of global keyword --> where user wants to create a variable inside the function
 ##directly and carry forward the updated value we need to use global variable.

'''a=6
def final():
    global a,b
    print("inside value is",a)
    a=7
    print("updated value is",a)
   #global b
    b=15
    b+=a
    print("value of b is",b)
final()
print("a value is",a)
print("b value is",b)'''
