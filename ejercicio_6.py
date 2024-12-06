texto=input("Ingrese su texto")
texto=texto.lower()
def ordenar_palabras(texto):
    lislet=texto.split()
    lislet.sort()
    print(lislet)
ordenar_palabras(texto)
