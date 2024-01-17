import matplotlib.pyplot as plt
Year = [1980,1990,2000,2010,2020]
Unemployment_Rate = [6.2,5.9,6.5,6.5,6.2]
plt.plot(Year,Unemployment_Rate,color= 'r',marker='h')
plt.title('halat kharab')
plt.xlabel('year')
plt.ylabel('unemployment rate')
plt.grid('true')
plt.show()
