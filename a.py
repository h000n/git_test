import re
f = ''.join([i if ord(i) < 128 else ' ' for i in a])
j=f.replace("function","\nfunction")
with open("a.txt","w",encoding="utf8") as bogo:
    bogo.write(j)