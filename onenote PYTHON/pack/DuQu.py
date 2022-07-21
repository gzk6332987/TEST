filename = 'text.txt'
f = open(filename,'r')
line = f.readlines()

txt = []
for line_s in line:
    x = line_s.strip('\n')
    txt.append(x)
print(txt)
