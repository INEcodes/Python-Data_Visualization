import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

iris = sns.load_dataset('iris')

ax = sns.swarmplot(x='species', y='sepal_length', data=iris)

plt.title("Iris swarmplot")
plt.show()