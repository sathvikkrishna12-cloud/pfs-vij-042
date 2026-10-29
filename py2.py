Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Indexing
a="vijayawada"
a[0]
'v'
a[5]
'a'
a[2]
'j'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'vijaya'
a="I am in class"
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[2]+a[3]
'am'
a[5]+a[6]
'in'
a[1]
' '
a[0]
'I'
a="Vijayawada is a royal city"
a[16]+a[17]+a[18]+a[19]+a[20]
'royal'
a[22]+a[23]+a[24]+a[25]
'city'
a[11]+a[12]
'is'
#Indexing(Negative)
a="Vizag is a city of destiny"
a[-15]+a[-14]+a[-13]+a[-12]
'city'
a[-26]+a[-25]+a[-24]+a[-23]+a[-22]
'Vizag'
a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'destiny'
a="Simple is better than complex"
a[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
'better'
a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'complex'
a[-29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
'Simple'

#Slicing(Positive)
a="Codegnan"
a[0:3]
'Cod'
a[0:4]
'Code'
a[4:8]
'gnan'
a[:4]
'Code'
a[6:]
'an'
a[4:]
'gnan'
a="Work hard until you suceed"
a[10:15]
'until'
a[5:9]
'hard'
a[0:4]
'Work'
a[16:19]
'you'
a[20:26]
'suceed'
a[20:]
'suceed'
a[:4]
'Work'
#Slicing(Negative)
a="I love python"
a[-11:-7]
'love'
a[-6:0]
''
a[-6:-1]
'pytho'
a[:-6]
'I love '
a[-6:]
'python'
b="Today is weekend"
a[-16:-11]
'I '
b[-16:-11]
'Today'
b[-10:-8]
'is'
b[-7:]
'weekend'
#Striding
a="data science"
a
'data science'
a[::]
'data science'
a[::1]
'data science'
a[::2]
'dt cec'
a="Machine Learning"
a[::4]
'MiLn'
a[::6]
'Men'
a[::2]
'McieLann'
a[5:]
'ne Learning'
a[:9]
'Machine L'
a[::7]
'M n'
>>> a="Cloud Computing"
>>> a[1:11:2]
'lu op'
>>> a[2:14:4]
'oCu'
>>> a[5:13:3]
' mt'
>>> A[4:12:2]
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    A[4:12:2]
NameError: name 'A' is not defined. Did you mean: 'a'?
>>> a[4:12:2]
'dCmu'
>>> #Striding(Negative)
>>> a="Python Course"
>>> a[-1:-11:-2]
'ero o'
>>> a[-2:-12:-3]
'sont'
>>> a[::-1]
'esruoC nohtyP'
>>> a[::1]
'Python Course'
