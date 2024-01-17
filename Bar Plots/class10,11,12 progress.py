#Try to improve this

import matplotlib.pyplot as plt
import numpy as np
x=[[73.0,94.0,85.0],[60.0,70.0,44.0],[60.0,80.0,75.0],[100.0,90.0,99.0],[98.0,97.0,96.0]]
value=np.arange(3)

plt.bar(value,x[0],color='b',width=0.25)
plt.plot(value,x[0],color='b',marker='s',markersize=6)


plt.bar(value+6,x[1],color='r',width=0.25)
plt.plot(value+6,x[1],color='r',marker='s',markersize=6)


plt.bar(value+12,x[2],color='y',width=0.25)
plt.plot(value+12,x[2],color='y',marker='s',markersize=6)


plt.bar(value+18,x[3],color='m',width=0.25)
plt.plot(value+18,x[3],color='m',marker='s',markersize=6)


plt.bar(value+24,x[4],color='g',width=0.25)
plt.plot(value+24,x[4],color='g',marker='s',markersize=6)

plt.xlabel(['student 1','student 2','student 3','student 4','student 5'])  


plt.ylabel('%age')
plt.show()
