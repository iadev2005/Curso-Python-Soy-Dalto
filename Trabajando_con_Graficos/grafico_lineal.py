import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv("Trabajando_con_Graficos\\pedos.csv")

sns.lineplot(x="fecha",y="pedos",data=df)
plt.show()
# Creando un punto en el grafico (No funcionó)
plt.plot("01-06",7,"o")
plt.plot("01-12",7,"o")
