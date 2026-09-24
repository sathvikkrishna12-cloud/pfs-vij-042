Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variables
print(9+2)
11
a=12
b=31
print(a+b)
43
Y=34
print(Y)
34
print(Z)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(Z)
NameError: name 'Z' is not defined
z=256
print(z)
256
2=40
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a2=34
print(a2)
34
4x=00
SyntaxError: invalid decimal literal
A012345678911=34
print(A012345678911)
34
name="Daredevil"
print(name)
Daredevil
print("name")
name
city="vij"
city
'vij'
country= "carrabien ✨"
country
'carrabien ✨'
a=007
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
a=7
b=3
print(a+b)
10
print(a-b)
4
fname= "Daredevil☠️"
lname= "Mr"
print(fname+lname)
Daredevil☠️Mr
print(fname" " lname)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(fname+" "+lname)
Daredevil☠️ Mr
a=10,b=35
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=10;b=25
print(a+b)
35
print(a+" " +b)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print(a+" " +b)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
a,b = 2,3
print(a+b)
5
a=345
b=45
print(a+b)
390
@=21
SyntaxError: invalid syntax
$=31
SyntaxError: invalid syntax
a,b,c=10
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    a,b,c=10
TypeError: cannot unpack non-iterable int object
_56
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    _56
... NameError: name '_56' is not defined
... p
... _=56
... print(_)
... 56
... _a=45
... print(_a)
... 45
... >>> a,c,d=2,3,4
... >>> print(a,c,d)
... 2 3 4
... >>> a=(1,2,3)
... >>> print(a)
... (1, 2, 3)
... >>> a,b,c=(4,3,2)
... >>> print(a,b,c)
... 4 3 2
... >>> a=56
... >>> print(a)
... 56
... >>> del a
... >>> print(a)
... Traceback (most recent call last):
...   File "<pyshell#59>", line 1, in <module>
...     print(a)
... NameError: name 'a' is not defined. Did you mean: 'a2'?
... >>> name="jacksparow"
... >>> print(name)
... jacksparow
... >>> Name=Aj
... Traceback (most recent call last):
...   File "<pyshell#62>", line 1, in <module>
...     Name=Aj
... NameError: name 'Aj' is not defined
... >>> Name="Aj"
... >>> print(Name)
... Aj
... >>> NAME="AJ"
... >>> print(NAME)
