Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#String Methods
a="chaitanya"
len(a)
9
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
#count()
a="Twinkle twinkle little star"
a.count("twinkle")
1
a.count("a")
1
a.count(" ")
3
a.count("i")
3
#Find a string
a="python"
a.find('h')
3
a.find('n')
5
b="hello"
b.find('l')
2

#Escape sequences
#\n= new line
#\t= tab space
a="name:me\nmobile no:98480\tcollege:abcd\nmail id:abcs@gmail.com\tbranch:DS"
print(a)
name:me
mobile no:98480	college:abcd
mail id:abcs@gmail.com	branch:DS

#replace()
a="wait until you succeed"
a.replace('wait','work')
'work until you succeed'
b="python full stack"
b.replace('python','java')
'java full stack'
b
'python full stack'
c=b.replace('python','java')
c
'java full stack'

#upper(),lower()
a="Code"
a.upper()
'CODE'
a.lower()
'code'
a[0].lower()
'c'
a="python dsa"
a.capitalize()
'Python dsa'
a.title()
'Python Dsa'
a="java"
a.isupper()
False
a.islower()
True
a="Java"
a.islower()
False
b='data science'
b.startswith('d')
True
b.endswith('e')
True
b.isalpha()
False
a="1234"
a.isdigit()
True
a.isalnum()
True
a="chai@375"
a.isalnum()
False
b='chai375'
b.isalnum()
True

#strip()-> 1)lstrip() 2)rstrip()
a="    Chaitanya     "
a.strip()
'Chaitanya'
a.lstrip()
'Chaitanya     '
a.rstrip()
'    Chaitanya'

#concatenation
a="Java"
b='full stack'
print(a+b)
Javafull stack
print(a+" "+b)
Java full stack
fname="B"
lname="Chaitanya"
print(fname.capitalize()+" "+lname.cpitalize())
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    print(fname.capitalize()+" "+lname.cpitalize())
AttributeError: 'str' object has no attribute 'cpitalize'. Did you mean: 'capitalize'?
print(fname.capitalize()+" "+lname.capitalize())
B Chaitanya
print(fname.strip()+" "+lname.strip())
B Chaitanya
print((fname+" "+lname).strip())
B Chaitanya

#split()
a="c c++ python java sql"
a.split()
['c', 'c++', 'python', 'java', 'sql']
print((fname+" "+lname).title())
B Chaitanya

#join()
" ".join(a)
'c   c + +   p y t h o n   j a v a   s q l'
"".join(a)
'c c++ python java sql'
c="c","c++",'java'
"".join(c)
'cc++java'
" ".join(c)
'c c++ java'
"l".join(c)
'clc++ljava'
d="java"
"1".join(d)
'j1a1v1a'

#formatting
a=1
b=2
print(a+b)
3
print("The sum off a and b is",a+b)
The sum off a and b is 3
city="Tenali"
print("The city i live is",city)
The city i live is Tenali

#format method()
a="motu"
b="patlu"
print("hello {}{}".format(a,b))
hello motupatlu
print("hello {} {}".format(a,b))
hello motu patlu
print("hello {} hello {}".format(a,b))
hello motu hello patlu
print(("hello {} hello {}".format(a,b)).title())
Hello Motu Hello Patlu
print("hello {} hello {}".format(a,b).title())
Hello Motu Hello Patlu

#fstring
a="motu"
b="patlu"
>>> print(f"hello {a} {b})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f"hello {a} {b}")
...       
hello motu patlu
>>> print(f"hello {a} hello {b}")
...       
hello motu hello patlu
>>> print((f"hello {a} hello {b}").title())
...       
Hello Motu Hello Patlu
>>> #TASK
...       
>>> a=10
...       
>>> b=20
...       
>>> print("Multiplication of {} and {} is {}".format(a,b,a*b))
...       
Multiplication of 10 and 20 is 200
>>> print(f"Multiplication of {a} and {b} is {a*b}")
...       
Multiplication of 10 and 20 is 200
