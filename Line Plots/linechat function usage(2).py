import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,3.15,0.1)
y=np.sin(x)
plt.plot(x,y,ls='dotted',marker='D',color='r')
plt.show()
