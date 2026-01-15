'''
Practica 3
Imprimir la tabla de multiplicar del x utilizando ciclo for
'''


x = input("Introduzca un numero")


for i in range(1,11):
    multiplicacion = int(x) * i

    print(x," X ", i ," = ", multiplicacion)

