import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,6,100)
y = (2*x-5)**2-1

def J(x):
    return  (2*x-5)**2-1

def dJ(x):
    return 4*(x-5)

x0= 0.0
eta = 0.3
x_history=[]
i=0
while i<100:
    dJ1 = dJ(x0)
    if abs(dJ1) < 1e-6:
        break
    x0=x0-eta*dJ1
    x_history.append(x0)
    i=i+1
#print(x_history)
plt.plot(x,y)
plt.plot(np.array(x_history),J(np.array(x_history)),color = 'r',marker = '+')
plt.show()

