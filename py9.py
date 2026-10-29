#List comprehension
'''a=['python','java','dsa']'''

#print(a.upper()) ##error

'''b=str(a)
print(b.upper())'''

'''for i in a:
    print(i.upper(),end=",")'''

#syntax
#a=[expr for var in collection/range]

'''b=[i.upper() for i in a]
print(b)'''

'''a=['hyd','vja','vzg']
a=[i.capitalize() for i in a]
print(a)'''

'''a=[1,2,3,4,5,6,8,12,13]
a=[pow(i,2) for i in a] # or i**2 or i*i
print(a)'''

#range=21

'''a=[i for i in range(21)]
print(a)'''

#if-usage in list comprehension

'''a=[i for i in range(16) if i%2==0]
print(a)'''

'''a=[i*i for i in range(16) if i%2==0]
print(a)'''

'''a=['apple','grapes','kiwi','mango','dragon','berry']
b=[i for i in a if "a" in i]
print(b)'''

'''a=['apple','grapes','kiwi','mango','dragon','berry']
b=[i for i in a if "a" not in i]
print(b)'''

#no-elif usage in list comprehension
#if-else usage in list comprehension

#range=31 print i^2 if even else i*5

'''a=[i*i if i%2==0 else i*5 for i in range(31)]
print(a)'''

'''a=[1,2,3,4,5]
b=[5,4,3,2,1]
#[6,6,6,6,6]
##c=[a[i]+b[i] for i in range(5)]
c=[a[i]+b[i] for i in range(len(a))]
print(c)'''

#max(),min(),sum()

'''print(max(10,50,77,67))
print(min(10,50,77,67))
a=[10,20,30]
print(sum(a))
print(sum([5,6]))'''

#---------------------Marks Analysis Report--------------------------#

a=int(input("No.of Students:"))
b=[]
for i in range(a):
    b.append(int(input(f"stu{i+1} marks:")))
print("Marks Analysis Report........")
print("Total no of students =",a)
print(f"Highest Marks={max(b)}")
print(f"Lowest Marks={min(b)}")
print(f"Total Marks={sum(b)}")
print(f"Average Marks={sum(b)/a}")
