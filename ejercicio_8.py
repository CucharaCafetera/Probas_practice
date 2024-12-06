from matplotlib import pyplot as plt
valores= [30,25,20,25]
etiquetas=['Manzanas','Naranjas','Plátanos','Uvas']
colores=["tab:purple","tab:green", "tab:red","tab:blue",]
label=['Manzanas','Naranjas','Plátanos','Uvas']
plt.pie(valores,labels=label,autopct='%1.1f%%',colors=colores)
plt.legend(label,title="Frutas")
plt.title("Frutas")
plt.show()


