#if-elif-else
#comparison

'''a=3
b=6
if a<b:
    print("less")
elif a>b:
    print("greater")
else:
    print("true")'''

'''a=3
b=6
if a==b:
    print("less")
elif a>b:
    print("greater")
else:
    print("true")'''

'''a=7
b=6
if a<b:
    print("less")
elif a>b:
    print("greater")
else:
    print("true")'''

'''a=6
b=6
if a<b:
    print("less")
elif a>b:
    print("greater")
elif a==b:
    print("equal")
else:
    print("true")'''

#logical

'''a=int(input())
b=int(input())
if a<b or b>a:
    print("less")
elif a>b and b<a:
    print("greater")
elif not a!=b:
    print("equal")
else:
    print("true")'''

#identical

'''a="abc"
if type(a)is int:
    print("int")
elif type(a) is float:
    print("float")
elif type(a) is not(int and float):
    print("string")
else:
    print("complex")'''

#membership

'''a=[10,20,30,40,50,60,70,90]
b=[80]
c=int(input("Enter search value:"))
if c in a:
    print("it is in a")
elif c in b:
    print("it is in b")
elif c not in(a and b):
    print("not present in both")
else:
    print("Inavalid")'''

#multiple-if
#comparison

'''a=4
b=8
if a<b:
    print("less")
if b>a:
    print("greater")
if(a!=b):
    print("!=")'''

#logical

'''a=4
b=4
c=4
if a<b or a<c:
    print("a is greater")
if(a==b and b==c):
    print("all are equal")
if not c!=a+b:
    print("c=a+b")'''

#identify

'''a="vijay"
if type(a) is int:
    print("int")
if type(a) is float:
    print("float")
if type(a) is not(int and float):
    print("String")'''

#membership

'''a=[10,20,30,40,50,60,70,80,90]
b=[1,2,3,4,5,6]
c=int(input("enter value:"))
if(c in a):
    print("it is in a")
if(c in b):
    print("it is in b")
if(c not in (a and b)):
    print("Not there")'''

#Nested-if conditions
#comparison

'''a=5
b=10
if a<b:
    print("less")
    if(b>a):
        print("greater")'''

'''a=5
b=10
if a==b:
    print("less")
    if(b>a):
        print("greater")'''

'''a=5
b=10
if a<b:
    print("less")
    if(b==a):
        print("equal")'''

'''a=30
b=40
if a<b:
    print("less")
    if(b==a):
        print("greater")
    else:
        print("true")'''

'''a=6
b=12
if(a>b):
    print("greater")
    if(b>a):
        print("less")
else:
    print("true")'''

'''a=2
b=4
if a==b:
    print("equal")
    if b<a:
        print("greater")
    else:
        print("true")
else:
    print("False")'''

#tasks
#1

'''a=int(input("enter age of voter:"))
if(a>=18):
    print("Eligible for vote")
else:
    print("Not eligible to vote")'''

#2

'''a=int(input("enter value:"))
if(a%2==0):
    print("Even")
else:
    print("Odd")'''

#3

'''a=int(input("enter year:"))
if(a%4==0):
    print("Leap year")
else:
    print("Non-leap year")'''

#4

'''a=input("Enter name:")
if(a=="chaitanya"):
    print(f"Welcome {a}")
else:
    print("Welcome Guest")'''

'''a=["a","b","c",'d','e']
b=input("enter name:")
if(b in a):
    print(f"Welcome {b}")
else:
    print("Welcome Guest")'''

#5

'''a=input("Enter a alphabet:").lower()
if(a=="a" or a== "e" or a== "i" or a== "o" or a== "u"):
    print("it is vowel")
else:
    print("it is consonant")'''

'''a=['a','e','i','o','u']
b=input("Enter a alphabet:").lower()
if(b in a):
    print("it is vowel")
else:
    print("it is consonant")'''

#6

'''a=int(input("Enter the price of cake:"))
if(a==1200):
    print("Red velvet")
elif(a==1000):
    print("Choco Almond")
elif(a==1000):
    print("Chocolate")
elif(a==600):
    print("Butter scotch")
else:
    print("cake is not available")'''

#7

'''a=input("Enter the pizza name:").lower()
if(a=="bbq pizza"):
    print(800)
elif(a=="crispy chicken pizza"):
    print(600)
elif(a=="panner pizza"):
    print(400)
elif(a=="corn pizza"):
    print(300)
elif(a=="french fries & coke"):
    print(200)'''

#8

'''a=int(input("Enter age:"))
b=int(input("Enter marks:"))
c=int(input("Enter attendance %:"))
if(a>=18):
    print("Eligible for vote")
if(b>=80):
    print("Eligible for scholarship")
if(c>=80):
    print("Allow to write exams")'''

#9

'''a=input("Enter username:")
b=int(input("Enter password:"))
if(a=="chaitanya"):
    if(b==142):
        print("login successful")
    else:
        print("Invalid password")
else:
    print("Invalid username")'''

'''a=input("Enter username:")
b=int(input("Enter password:"))
if(a=="chaitanya" and b==142):
    print("login successful")
else:
    print("Invalid credentials")'''
