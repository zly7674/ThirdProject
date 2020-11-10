import time
from collections import deque
Dq=deque()
#前插
start=time.clock()
for i in range(10000):
    Dq.appendleft(i)
end=time.clock()
print(end-start,'前插')
#后插
start=time.clock()
for i in range(10000):
    Dq.append(i)
end=time.clock()
print(end-start,'后插')
#后删
for i in range(10000):
    Dq.append(i)
start=time.clock()
while i:
    Dq.pop()
    i=i-1
end=time.clock()
print(end-start,'后删')
#前删
start=time.clock()
while i:
     Dq.popleft()
     i=i-1
end=time.clock()
print(end-start,'前删')
