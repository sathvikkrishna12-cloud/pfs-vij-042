Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arithmetic
a=2
b=6
print(a+b)
8
print(b-a)
4
print(a*b)
12
print(a//b)
0
print(a/b)
0.3333333333333333
print(a**b)
64
print(a%b)
2
print(b%a)
0
print(b/a)
3.0
print(b//a)
3
#assignment
a=3
b=5
b+=a
b
8
b-=5
b
3
b*=5
b
15
b//=3
b
5
b/=2
b
2.5
b**=3
b
15.625
b%=7
b
1.625
#Relational/Comparison
a=5
b=7
a>b
False
a<b
True
a<=b
True
a>=b
False
b<=a
False
b>=a
True
a!=b
True
a==b
False
b=5
a==b
True
b!=a
False
#Logical
a=10
b=15
a<b and b>a
True
a>b and b>a
False
a<=b and b>=a
True
a!=b and b==a
False
a<b or b>a
True
a<=b or b<=a
True
a!=b or b==a
True
not True
False
not False
True

#Identify/Identity
a=5.5
type
<class 'type'>
type(a) is int
False
type(a) is not int
True
type(a) is not float
False
type(a) is float
True

a=cha
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a=cha
NameError: name 'cha' is not defined. Did you mean: 'chr'?
a="cha"
type(a) is str
True
a=True
type(a) is bool
True

#Membership
a=2,4,6,8,0,10,5
9 in a
False
19 not in a
True
4 in a
True
0 not in a
False

#Bitwise
a=3
b=6
a&b
2
bin(2)
'0b10'
bin(b)
'0b110'
a|b
7
a^b
5
b=7
a|b
7
>>> a=5
>>> -(a+1)
-6
>>> ~a
-6
>>> a=-7
>>> ~a
6
>>> -(a+1)
6
>>> a=3
>>> b=7
>>> a^b
4
>>> a<<3
24
>>> a>>3
0
>>> a=9
>>> a>>3
1
>>> a<<3
72
