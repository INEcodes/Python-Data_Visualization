import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df =pd.read_csv("C:/Users/ADMIN/Documents/GitHub/Python-SKLearn/Iris_Flower_kaggle/IRIS.csv")
data = np.asarray(df['sepal_length']).reshape(150,1)
sns.heatmap(data)
plt.show()
sns.kdeplot(y=df['sepal_length'], x=df['petal_length'] ,color='green',fill = True)
plt.show()