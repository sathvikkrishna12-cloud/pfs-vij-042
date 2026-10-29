Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Dictionary
#dict{}
a={"name":"chaitanya","year":2005,"month":6}
type(a)
<class 'dict'>
a
{'name': 'chaitanya', 'year': 2005, 'month': 6}
#Note: The Difference between dict and set is the dict is always has a pair set of data a={a:b,c:d} whereas set is a={a,b,c,d}
a.keys()
dict_keys(['name', 'year', 'month'])
a.values()
dict_values(['chaitanya', 2005, 6])
a.items()
dict_items([('name', 'chaitanya'), ('year', 2005), ('month', 6)])
b=a.copy()
b
{'name': 'chaitanya', 'year': 2005, 'month': 6}
#Accessing -->a[""],a.get("")
a["name"]
'chaitanya'
a.get("year")
2005
#In this a["key"] must enter if a["value"] gives error and as well as dict is mutable but it doesnt allow duplicates
a.pop("year")
2005
a
{'name': 'chaitanya', 'month': 6}
a.popitem()
('month', 6)
a
{'name': 'chaitanya'}
#pop() function can delete specific mentioned key pair where as popitem() will delete last pair in the dict.
b
{'name': 'chaitanya', 'year': 2005, 'month': 6}
b.update({"course":"python"})
b
{'name': 'chaitanya', 'year': 2005, 'month': 6, 'course': 'python'}
b.update({"duration":100,"city":"vja"})
b
{'name': 'chaitanya', 'year': 2005, 'month': 6, 'course': 'python', 'duration': 100, 'city': 'vja'}
#Update function to enter multiple entries we should give , in between pairs in a single argument like a.update({a:b,c:d,e:f})
a
{'name': 'chaitanya'}
a.setdefault("year",2005)
2005
a
{'name': 'chaitanya', 'year': 2005}
#setdefault() we can only update one set of pair but the format(:) is not necessary like as a.setdefault(key,pair) while normally we update a.update({key:pair}).
b.copy()
{'name': 'chaitanya', 'year': 2005, 'month': 6, 'course': 'python', 'duration': 100, 'city': 'vja'}
len(b)
6
b.clear()
b
{}
#In dict and set there are no methods to count and index due to both are inorder and doesnt have duplicates.
a={"age":5,"age":5}
a
{'age': 5}
>>> a={"age":5,"age":10}
>>> a
{'age': 10}
>>> a={"age1":5,"age":10}
>>> a
{'age1': 5, 'age': 10}
>>> 
>>> a={"idnos":[10,20,30],"names":[a,b,c]}
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a={"idnos":[10,20,30],"names":[a,b,c]}
NameError: name 'c' is not defined
>>> a={"idnos":[10,20,30],"names":['a','b','c']}
>>> a
{'idnos': [10, 20, 30], 'names': ['a', 'b', 'c']}
>>> type(a)
<class 'dict'>
>>> a.keys()
dict_keys(['idnos', 'names'])
>>> a.values()
dict_values([[10, 20, 30], ['a', 'b', 'c']])
>>> a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['a', 'b', 'c'])])
