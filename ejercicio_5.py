palabra=input("Ingrese su palabra: ")
palabra= palabra.lower()
def palindromo(palabra):
    palabraes= " ".join(palabra) 
    listpa= palabraes.split()
    listpa_2= palabraes.split()
    listpa.reverse()
    cdef=int(0)
    c=int(0)
    while c < len(listpa):
        if listpa[c] == listpa_2[c]:
            cdef+=1
        else :
            pass
        c+=1
    if cdef==len(listpa):
        print("Su palabra es un palíndromo")
    else:
        print("Su palabra no es un palíndromo")

palindromo(palabra)
