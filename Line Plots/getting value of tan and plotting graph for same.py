import matplotlib.pyplot as plt
import numpy as np
x=int(input('enter a number'))
y=np.tan(x)
plt.plot(y,x,marker='D',markersize=5)
print('value of the tan of x is:',y)
plt.show()
