#Striplot:
#this does like a scatterplot in the seaborn library but it does it categorically

import matplotlib.pyplot as plt
import seaborn as sns

X=['First','Second','Third','Fourth','Fifth','Sixth']
Y=[10,9,8,7,6,5]

ax = sns.stripplot(x=X, y=Y);

ax.set(xlabel = 'Category', ylabel='Values')
plt.title("SNS Strip_Plot");
plt.show()