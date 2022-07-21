n = int(input(">>>"))
aa = []
bb = []
for i in range(n//2):
    a = i
    b = n - i

    aa.append(a)
    bb.append(b)
o = zip(aa,bb)
oo = list(o)
print(oo)