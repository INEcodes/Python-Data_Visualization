

import matplotlib.pyplot as plt
x=['IP','IP','IP','PE','PE','IP','IP','IP','IP','IP','PE','PE']
plt.hist(x,bins=2,orientation='horizontal',label=['green','orange'],edgecolor='y')
plt.xticks(['IP'])