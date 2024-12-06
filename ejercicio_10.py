from matplotlib import pyplot as plt
x=[1,2,3,4,5]
y=[2,3,5,7,11]
tamaños=[20,50,80,100,150]
plt.scatter(x=x,y=y,s=tamaños,marker='*')
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.show()