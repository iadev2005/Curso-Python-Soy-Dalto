import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv("Trabajando_con_Graficos\\cofla_ingresos.csv")

sns.barplot(x="fuente",y="ingresos",data=df)
total_ingresos = df["ingresos"].sum()

# Mostrando el total
print(f"El total de ingresos es de: ${total_ingresos} USD")

# Mostrando gráfico
plt.show()
