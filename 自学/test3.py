import re
s='2342werwre2342werwrew'
p=r'(\d*)([a-zA-Z]*)'
m=re.match(p,s)
print(m.group())
