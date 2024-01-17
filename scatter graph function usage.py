import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,3.15,1)
y=np.tan(x)
plt.scatter(x,y,marker='o',c='r',s=1000)
plt.show()