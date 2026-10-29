#Generators
#No tuple comprehension in above cases if we remove those braces and keep paranthesis
 ##the the outcome is generator.
#List Comprehension syntax --> a=[expr for var in collection/range]

'''a=[i for i in range(16)]
print(a)
print(type(a))'''

'''a=(i for i in range(21))
#print(a) #doesn't print output
#print(*a)
#print(type(a))

#print(list(a))
#print(type(a))

#print(tuple(a))
print(set(a))'''

#Generator Definition --> A generator is also a function which can be also use as
 ##iterator(loops) by producing loop of values where we can use yield keywords.

#Yield v/s Return --> Return will terminate the function whereas Yield can pass the
 ##function and go on with every sucessive iteration. 

'''a,b=[int(i) for i in input("Enter the values:").split(",")]
def check(a,b):
    while a<b:
        yield a #if 2,9 gives [2 to 8]
        a+=1
        #yield a #if 2,9 gives [3 to 9]
print(*check(a,b))'''

'''a,b=[int(i) for i in input("Enter the values:").split(",")]
def check(a,b):
    while a<b:
        a+=1
        #return a
    return a
print(check(a,b))'''

#yield v/s return

'''def mygen():
    #return "vja"
    #return 'hyd'
    #return 'vzg'
    return 'vja','hyd','vzg'
print(*mygen())'''

'''def mygen():
    yield 'apple'
    yield 'mango'
    yield 'grapes'
print(*mygen())
#next()
d=mygen()
print(next(d))
print(next(d))
print(next(d))
print(next(d))''' #error due to completion of iteration in previous step. 

#BMI calculator task

'''while True:
    a=float(input("Enter the height(in cm):"))
    b=float(input("Enter the weight:"))
    r=(b/(a/100)**2)
    if(r<=18.5):
        print("Under weight")
    elif(r>18.5 and r<=24.5):
        print("Normal weight")
    elif(r>24.5 and r<=29.5):
        print("Over weight")
    else:
        print("Obesity")'''

#fromkeys()

'''a="codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))
#print(dict(a)) #error

b=dict.fromkeys(a)
print(b)

b=dict.fromkeys(a,"bcsns")
print(b)

b['o']="chai"
print(b)'''

#eval()

'''while True:
    a=int(input("a value:"))
    b=int(input("b value:"))
    print(a+b)'''

'''while True:
    a=float(input("a value:"))
    b=float(input("b value:"))
    print(a+b)'''

'''while True:
    a=input("a value:")
    b=input("b value:")
    print(a+b)'''

'''while True:
    a=eval(input("a value:"))
    b=eval(input("b value:"))
    print(a+b)'''

#zip()-->we can combine multiple collections into one collection.

'''a=[10,20,30,40,50]
names=["venkat",'ajay','teja','harsha','prasad']
print(a+names)

b=zip(a,names)
print(b)

c=list(zip(a,names))
print(c)

d=tuple(zip(a,names))
print(d)

e=set(zip(a,names))
print(e)

f=dict(zip(a,names))
print(f)'''

#enumerate()-->we can give counter to the collection.

'''names=["venkat",'ajay','teja','harsha','prasad']
for i in range(len(names)):
    print(i,names[i])

b=list(enumerate(names,1))
print(b)

c=dict(enumerate(names,100))
print(c)'''

#map-->each object from a collection and forms of new collection.

'''a=[2,5,7,9,10,12,15,20]
b=[1,3,6,8,17,25,40,60]

c=list(map(max,a,b))
print(c)

d=list(map(min,a,b))
print(d)'''

#Anonymous function -->anonymous or nameless functions and we use a key word called as lambda
 ##to create anonymous functions.

#write a funcyion to calculate 2*x+5 where x=5.

'''def check(x):
    return ((2*x)+5)
x=int(input())
print(check(x))'''

'''def cal():
    x=int(input("value:"))
    print(2*x+5)
cal()'''

#syntax ---> a=lambda arg:expr
'''a=lambda x:2*x+5
print(a(5))'''

'''a=int(input("Enter a value:"))
b=lambda x:x*2+5
print(b(a))'''

'''a="python"
b=lambda x:(x.upper())
print(b(a))'''

'''a="hello world"
b=lambda x:(x.title())
print(b(a))'''

'''fname=input("fname:")
lname=input("lname:")
f=lambda fname,lname:(fname+" "+lname).title()
print(f(fname,lname))'''

'''f,l=[str(i) for i in input("name").split(" ")]
r=lambda f,l:(f+" "+l).title()
print(r(f,l))'''

'''a,b=map(int,input("Enter the numbers:").split())
f=lambda a,b:a**b
print(f(a,b))'''

#filter()

'''a=[2,6,8,10,13,15,20,27,40,60,87,100]
for i in a:
    if(i%2==0):
        print(i,end=" ")'''

'''a=[2,6,8,10,13,15,20,27,40,60,87,100]
b=tuple(filter(lambda x:x%2==0,a))
print(b)'''

'''a=[[],(),set(),{},""," ",None,3,7.8,'python',9+5j,True,False]
b=list(filter(None,a))
print(b)'''

'''a=input("data1:")
b=input("data2:")
print(a+b)'''

'''a,b=input("Enter the names:").split(",")
print(a+b)'''

'''a=[x for x in input("ENter the names:").split(",")]
print(a)'''

'''a,b=map(str,input("Enter the names:").split(","))
print(a+b)'''

'''a=int(input("a value:"))
b=int(input("b value:"))
print(a+b)'''

'''a,b=int(input("Enter the values").split())
print(a+b)''' #error

'''a,b=[int(x) for x in input("Enetr the values:").split(",")]
print(a+b)'''

'''a,b=map(int,input("Enter the values:").split(","))
print(a+b)'''

'''a=list(map(int,input("Enter the values:").split(",")))
print(a)'''

'''a=tuple(map(int,input("Enetr the values:").split(",")))
print(a)'''

'''a=set(map(int,input("Enetr the values:").split(",")))
print(a)'''

'''a=input("Enter the key and value pairs:")
b=dict(i.split(":") for i in a.split(","))
print(b)'''
