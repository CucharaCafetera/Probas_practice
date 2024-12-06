lista=[]
i=int(input("Ingrese el número de elementos a ingresar"))
c=0
while c<i:
    num=int(input("Ingrese el número"))
    lista.append(num)
    c+=1
def duplicados(lista):
    lista_final= []
    for x in lista:
        contador= 0
        for v in lista:
            if x == v:
                contador+=1
            else:
                pass
        if contador>1:
            lista_final.append(x)
    return lista_final
listf= set(duplicados(lista))
print(sorted(listf))
