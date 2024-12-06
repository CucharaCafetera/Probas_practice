cadena=input("Ingrese su texto")
def contar_vocales(cadena):
    vocales = ["a","e","i","o","u"]
    cadena.lower()
    cadenal= " ".join(cadena)
    listc= cadenal.split()
    c=0
    for x in vocales:
        for v in listc:
            if x==v:
                c+=1
            else:
                pass
    return c
print(contar_vocales(cadena))