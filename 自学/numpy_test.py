'''
import numpy as np

a = np.array([[1,2,3],
                  [2,3,4]
                   ],dtype=np.float16)
b = np.random.random()
'''
import numpy as np
import matplotlib.pyplot as plt
'''
mu = 1  #期望为1
sigma = 3  #标准差为3
num = 10000  #个数为10000

rand_data = np.random.normal(mu, sigma, num)
count, bins, ignored = plt.hist(rand_data, 30, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (bins - mu)**2 / (2 * sigma**2)), linewidth=2, color='r')
plt.show()
'''
import numpy as np
a = np.arange(2,14)
print(a)
print(np.zeros_like(a))




