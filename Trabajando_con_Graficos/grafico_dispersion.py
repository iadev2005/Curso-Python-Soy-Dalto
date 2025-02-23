import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv("Trabajando_con_Graficos\\dispersion.csv")

sns.scatterplot(x="tiempo",y="dinero",data=df)


# Mostrando gráfico
plt.show()
