import re
txt = " GET / HTTP/1.1"
# f = re.search(" (/.*) ",txt).group(1)
f = re.search(r"[ ][\w]*[ ](/[\w]*)[ ]", txt).group(1)
print(f)