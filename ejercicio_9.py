from matplotlib import pyplot as plt
x=[0,1,2,3,4,5]
y1=[0,1,4,9,16,25]
y2=[0,1,2,3,4,5]
plt.plot(x,y1,'o-r')
plt.plot(x,y2,'s-b')
leyendas=['y1','y2']
plt.legend(leyendas)
plt.show()