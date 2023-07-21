import matplotlib.pyplot as plt
agegroup = [10,15,20,25,30,35,12,40,15] 
plt.hist(agegroup,bins=10)
plt.xticks([10,20,30,40])
plt.xlabel('avg. population')
plt.ylabel('no of people')
