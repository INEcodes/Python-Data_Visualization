import matplotlib.pyplot as plt
import numpy as np
import random
y2=random.randint(1000,10000000)
x2=random.randint(100,10000000)
x1=np.random.randint(1,100,size=(6,))
y1=np.random.randint(1,100,size=(6,))
plt.scatter(x2,y2)
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.show()


