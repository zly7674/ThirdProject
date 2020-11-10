import time
Li=[]
#前插
start=time.clock()
for i in range(10000):
    Li.insert(0,i)
end=time.clock()
print(end-start)
#后插
start=time.clock()
for i in range(10000):
    Li.append(i)
end=time.clock()
print(end-start)
#后删
for i in range(10000):
    Li.append(i)
start=time.clock()
while i:
     Li.pop(i)
     i=i-1
end=time.clock()
print(end-start)
#前删
start=time.clock()
while i:
     Li.pop(10000-i)
     i=i-1
end=time.clock()
print(end-start)
