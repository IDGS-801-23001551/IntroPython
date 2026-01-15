'''
Practica 4
Pedir al usuario que ingrese 20 numeros repetidos y sin repetir
los almacene en una lista y luego muestre la lista ordenada de menor a mayor, tambien nos diga cuantos son repetidos y cuantas veces
se repitieron separarlos entre pareales e impares
'''
lista = []

for i in range(20):
    num = input("Introduzca el numero {} ".format(i+1))
    lista.append(int(num))
lista.sort()

print(lista[:])

v = 0 
pares = []
impares = []
ListaRepetidos = []
B = False

for i in range(20):
    x=lista[i]
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x) 

    for j in range(20):
        y=lista[j]
        if x==y:
            v+=int(1)        
    if v>1:    
        
        if x not in ListaRepetidos:     
            print("El numero ",x," sale", v, "veces")
            ListaRepetidos.append(x)
    v=0        
        
    
print("los numero pares son ", pares[:])
print("los numero impares son ", impares[:])    

    
