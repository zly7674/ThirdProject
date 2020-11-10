from moudle import Student as St
from moudle import Class as Cl

stua=St('zhao',90)
stub=St('liu',80)
stuc=St('wang',70)

cla=Cl()
cla.addstu(stua)
cla.addstu(stub)
cla.addstu(stuc)
cla.removestu(stuc)

cla.showname()
cla.maxscore()
