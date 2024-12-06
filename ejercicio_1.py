lista=[]
suma=0
n=int(input("Ingrese el número de elementos que desea ingresar en la lista"))
c=0
num=0
while c<n:
    num= int(input("Ingrese un número"))
    lista.append(num)
    if (c+1)%2==0:
        suma+=num
    c+=1
print(suma)