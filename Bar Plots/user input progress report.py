import matplotlib.pyplot as plt
import numpy as np
x=int(input('enter your 10th marks'))
x1=int(input('enter your 11th marks'))
x2=int(input('enter your 12th marks'))
y=[x,x1,x2]
value=np.arange(3)
plt.bar(value,y,color='y',width=0.25)
plt.plot(value,y,color='y',marker='s',markersize=6)
plt.ylabel('%age')
plt.xlabel('progress')
plt.show()