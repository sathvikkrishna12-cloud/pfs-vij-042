'''a=10
b=20
print(a+b)
c=a+b
print(c)
print(10+20)'''

#int
'''a=int(input("A:"))
b=int(input("B:"))
print(a+b)'''

#float
'''a=float(input("A:"))
b=float(input("B:"))
print(a+b)'''

#string
'''a=str(input("str A:"))
b=str(input("str B:"))
print(a+b)'''

'''a=input("str A:")
b=input("str B:")
print(a+b)'''

#complex
'''a=complex(input("complex A:"))
b=complex(input("complex B:"))
print(a+b)'''

#Boolean
'''a=bool(input("bool A:"))
b=bool(input("bool B:"))
print(a+b)'''

#Sample examples
'''a=input("fname:")
b=input("lname:")
print((a+" "+b).title())'''

'''a=int(input("a value:"))
b=int(input("b value:"))
opt=int(input("choose the option 1.add\n2.sub\n3.mul:"))
if(opt==1):
    print(a+b)
elif(opt==2):
    print(a-b)
elif(opt==3):
    print(a*b)
else:
    print("Error")'''

#swapping in 4 methods
#1
'''a=10
b=20
a,b=b,a
print("a:",a)
print("b:",b)'''

#2
'''a=10
b=20
temp=a
a=b
b=temp
print("a:",a)
print("b:",b)'''

#3
'''a=10
b=20
a=a+b
b=a-b
a=a-b
print("a:",a)
print("b:",b)'''

#4
'''a=10
b=20
a=a+b
b=a-b
a=a-b
print("After swapping values a:%d b:%d"%(a,b))
print("After swapping values a:%f b:%f"%(a,b))
print("After swapping values a:%.2f b:%.2f"%(a,b))'''

#Tasks
'''a=float(input("Enter a:"))
b=float(input("Enter b:"))
a=a+b
b=a-b
a=a-b
print("After swapping")
print("a:%.2f b:%.2f"%(a,b))'''

'''a=input("Enter a:")
b=input("Enter b:")
temp=a
a=b
b=temp
print("After swapping")
print("a:%s b:%s"%(a,b))'''

'''a=int(input("Enter id no:"))
b=(input("Enter name:").title())
c=int(input("Enter ph no:"))
d=input("Enter mail id:")
e=(input("Enter college name:").title())
f=(input("Enter your Branch:").upper())
print("\nStudent Details")
print("ID no:%d\nName:%s\nPhone no:%d\nMail id:%s\nCollege:%s\nBranch:%s"%(a,b,c,d,e,f))
'''
