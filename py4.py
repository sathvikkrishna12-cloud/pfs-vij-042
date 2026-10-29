Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[3,4.5,"python",6+9j,True,False]
print(a)
[3, 4.5, 'python', (6+9j), True, False]
type(a)
<class 'list'>
#list methods
>>> a=["c","java","python"]
>>> a.append("c++")
>>> a
['c', 'java', 'python', 'c++']
>>> a.append(["ml",'ai'])
>>> a
['c', 'java', 'python', 'c++', ['ml', 'ai']]
>>> a=["c","java","python"]
>>> a.extend(["c++","sql"])
>>> a
['c', 'java', 'python', 'c++', 'sql']
>>> #insert()
>>> a.insert(3,"ML")
>>> a
['c', 'java', 'python', 'ML', 'c++', 'sql']
>>> a.index("java")
1
>>> c=a.copy()
>>> c
['c', 'java', 'python', 'ML', 'c++', 'sql']
>>> #sort()
>>> a.sort()
>>> a
['ML', 'c', 'c++', 'java', 'python', 'sql']
>>> b=[0,5,8,-1,7,9,11,13]
b.sort()
b
[-1, 0, 5, 7, 8, 9, 11, 13]
b.reverse()
b
[13, 11, 9, 8, 7, 5, 0, -1]
#pop(),remove(),clear()
a.pop()
'sql'
a
['ML', 'c', 'c++', 'java', 'python']
a.pop(0)
'ML'
a
['c', 'c++', 'java', 'python']
a.remove("c++")
a
['c', 'java', 'python']
a.clear()
a
[]
a.extend(["c",'c++','java'])
a
['c', 'c++', 'java']
len(a)
3
a.count('c')
1

#tuple()
a=(4,6.7,"abc",4+5j,True)
a
(4, 6.7, 'abc', (4+5j), True)
type(a)
<class 'tuple'>
a.count('abc')
1
a.index(True)
4
a.count(6.7)
1
a.index(4)
0

#sets{}
s={3,6.7,"python",9+2j,True,False}
s
{False, True, 3, 'python', 6.7, (9+2j)}
type(s)
<class 'set'>
a={4,5,6,7,8,9}
a.add(10)
a
{4, 5, 6, 7, 8, 9, 10}
a={1,2,3,4,5,6}
b={5,6,7,8,9,10}
a.issubset(b)
False
b.issubset(a)
False
a={2,3,4,5,6,7,8}
b={5,6,7,8}
a.issubset(b)
False
b.issubset(a)
True
a.issuperset(b)
True
a={4,5,6,7,8,9}
b={7,8,9}
a.issuperset(b)
True
b.issuperset(a)
False
b.issubset(a)
True
d={2,2,2,5,7,2,1,4}
d
{1, 2, 4, 5, 7}
#union()
a={1,2,3,4,5}
b={4,5,6,7,8}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8}
a
{1, 2, 3, 4, 5}
a.intersection(b)
{4, 5}
b
{4, 5, 6, 7, 8}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8}
a={5,6,7,8,9,10,11}
b={9,10,11,12,13,14}
a.difference(b)
{8, 5, 6, 7}
b.difference(a)
{12, 13, 14}
a.symmetric_difference(b)
{5, 6, 7, 8, 12, 13, 14}
a={4,5,6,7,8,9}
b={6,7,8,9,10,11}
a.difference_update(b)
a
{4, 5}
b.difference_update(a)
b
{6, 7, 8, 9, 10, 11}
a={1,2,3,4}
b={3,4,5,6}
a.intersection_update(b)
a
{3, 4}
b.intersection_update(a)
b
{3, 4}

a={10,20,30,40,50}
b={30,40,50,60,70}
a.symmetric_difference_update(b)
a
{20, 70, 10, 60}
b.symmetric_difference_update(a)
b
{50, 20, 40, 10, 30}
c={2,3,4,5,6,7,8}
c.pop()
2
c
{3, 4, 5, 6, 7, 8}
c.remove(5)
c
{3, 4, 6, 7, 8}
c.discard(7)
c
{3, 4, 6, 8}
c.clear()
c
set()
c.add(10)
c
{10}
c.add(25)
c
{25, 10}
a={1,2,3,4}
b={5,6,7,8}
c{1,2}
SyntaxError: invalid syntax
c={1,2}
a.isdisjoint(b)
True
a.isdisjoint(c)
False
b.isdisjoint(c)
True
b.isdisjoint(a)
True
len(a)
4
len(c)
2
