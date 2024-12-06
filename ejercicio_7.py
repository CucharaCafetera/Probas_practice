from statistics import mean,median,mode
"""list=[]
for x in range(0,25):
    num=int(input("Ingrese su número: "))
    list.append(num)
media= str(mean(list))
mediana=str(median(list))
moda= str(mode(list))
print("Su media es: " + media  + " Su moda es: " + moda + " Su mediana es: " + mediana)"""
from sympy import symbols,Function,Derivative,limit
x = symbols('x')
expr=x**2 + 3*x + 2
limite=limit(expr,x,9.5)
print(limite)
derivada=Derivative(expr,x)
derivada=derivada.doit()
print(derivada)
