import re

filename = '163小号.txt'
s = []
t = open(filename, "r")
for i in t.readlines():
    s.append(i.strip().strip())
ss = []
for i in s:
    if i == "":
        pass
    else:
        ss.append(i)

sss = []
number = 1

a = []
b = []

for i in ss:
    if number % 2 == 0:
        a.append(i)
        pass
    else:
        b.append(i)
        pass
    number += 1
    pass

cc = zip(b,a)
c = list(cc)

d1 = dict(c)

print(c)
print(d1)