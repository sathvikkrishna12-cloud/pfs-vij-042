#Conditions
#if-condition using comparison operators
#<,>,<=,>=,!=,==

'''a=10
b=15
if a<b:
    print("true")'''

'''a=10
b=15
if a>b:
    print("true")'''

'''a=10
b=15
if a<=b:
    print("true")'''

'''a=10
b=15
if a>=b:
    print("true")'''

'''a=10
b=15
if a!=b:
    print("true")'''

'''a=10
b=15
if a==b:
    print("true")'''

'''a=int(input("a value:"))
b=int(input("b value:"))
if a<b:
    print("less")'''

'''a=int(input("a value:"))
if a!=15:
    print("not equal")'''

'''a="python"
if a!="java":
    print("not match")'''

#if-condition using logical operators
#and,or,not

'''a=3
b=6
if a<b and b>a:
    print("true")'''

'''a=3
b=6
if a<=b and b>=a:
    print("true")'''

'''a=3
b=6
if a!=b and b==a:
    print("true")'''

'''a=3
b=6
if a<b or b>a:
    print("true")'''

'''a=3
b=6
if a<=b or b>=a:
    print("true")'''

'''a=3
b=6
if a!=b or b==a:
    print("true")'''

'''a=6
b=3
if not a<b:
    print("true")'''

'''a=6
b=3
if not a>b:
    print("true")'''

'''a=3
b=6
if not a<b and b>a:
    print("true")'''

'''a=int(input("a value:"))
b=int(input("b value:"))
if not a<b:
    print("true")'''

'''a="data science"
if not a=="python":
    print("true")'''

#if_condition using identity operators
#is,is not

'''a=4
if type(a) is int:
    print("true")'''

'''a=4
if type(a) is not int:
    print("True")'''

'''a=float(input("a value:"))
if(type(a) is not int):
    print("True")'''

'''a="chaitanya"
if(type(a) is str):
    print("String")'''


#if-condition using membership operators
#in,not in

'''a=2,3,4,5,6,7,8,9,10
if 10 in a:
    print("true")'''

'''a=2,3,4,5,6,7,8,9,10
if 20 in a:
    print("true")'''

'''a=2,3,4,5,6,7,8,9,10
if 20 not in a:
    print("true")'''

'''a=int(input("a value:"))
if 10 in a:
    print("true")'''#error

'''a=[2,3,4,5,6,7,8,9,10]
b=int(input("b value:"))
if b in a:
    print("true")'''

#if-else conditions using comparison operators

'''a=6
b=12
if a<b:
    print("True")
else:
    print("false")'''

'''a=6
b=12
if a==b:
    print("True")
else:
    print("false")'''

#if-else conditions using logical operators

'''a=6
b=12
if a<b and b>a:
    print("True")
else:
    print("false")'''

'''a=6
b=12
if a<b and b<a:
    print("True")
else:
    print("false")'''

'''=6
b=12
if a<b or b>a:
    print("True")
else:
    print("false")'''

'''a=6
b=12
if not a<b:
    print("True")
else:
    print("false")'''

#if-else conditions using identify operators

'''a=6
if type(a) is int:
    print("True")
else:
    print("false")'''

'''a=6
if type(a) is float:
    print("True")
else:
    print("false")'''

'''a=6
if type(a) is not float:
    print("True")
else:
    print("false")'''

'''a=6
if type(a) is not int:
    print("True")
else:
    print("false")'''

#if-else conditions using membership operators

'''a=[1,2,3,4,5,6,7,8,9]
if 10 in a:
    print("True")
else:
    print("false")'''

'''a=[1,2,3,4,5,6,7,8,9]
if 10 not in a:
    print("True")
else:
    print("false")'''
