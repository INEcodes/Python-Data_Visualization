import matplotlib.pyplot as plt
import seaborn as sns 

sns.distplot([0,1,2,3,4,5])#with histogram

sns.distplot([0,1,2,3,4,5], hist=False)#without histogram

iris = sns.load_dataset('iris')

sns.distplot(iris['sepal_length'])
plt.show()
'''
Distplot stands for distribution plot, it takes as input an array and plots a curve corresponding 
to the distribution of points in the array.
'''