import matplotlib.pyplot as plt 
import numpy as np
value=np.arange(5)
x=[1,3,6,7,9]
x1=[5,2,7,8,2] 
x2=[2,4,6,8,10]
x3=[8,6,2,5,6]
plt.bar(value,x,color='y',width=0.25)
plt.bar(value+5,x1,color='r',width=0.25)
plt.bar(value+10,x2,color='m',width=0.25)
plt.bar(value+15,x3,color='b',width=0.25)
plt.legend(['class1','class2','class3','class4','class5'])
plt.show()