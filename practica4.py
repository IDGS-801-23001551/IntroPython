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

repetido = -1 

for i in range(20):
    x=lista[i]
    for j in range(20):
        y=lista[j]
        if x==y:
            repetido+=1
        
    if repetido>0:    
        print("El numero ",x," se repite", repetido, "veces")
        repetido = -1

    
