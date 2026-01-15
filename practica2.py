'''
Crear un programa que tenga un menu con las siguientes opciones
'''
def suma():
    a = input("Ingresa el primer número: ")
    b = input("Ingresa el segundo número: ")
    suma = int(a)+int(b)
    print("Resultado de la suma:", suma)

def resta():
    a = input("Ingresa el primer número: ")
    b = input("Ingresa el segundo número: ")
    resta = int(a)-int(b)
    print("Resultado de la resta:", resta)

def multiplicacion():
    a = input("Ingresa el primer número: ")
    b = input("Ingresa el segundo número: ")
    multiplicacion = int(a)*int(b)
    print("Resultado de la multiplicación:", multiplicacion)

def division():
    a = input("Ingresa el primer número: ")
    b = input("Ingresa el segundo número: ")
    if b != 0:
        division = int(a)/int(b)
        print("Resultado de la división:", division)
    else:
        print("Error: no se puede dividir entre 0")

def salir():
    print("Seleccionaste salir")


def main():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    opcion = input("Elige una opcion")

    if opcion == "1":
         suma()
    if opcion == "2":
         resta()
    if opcion == "3":
         multiplicacion()
    if opcion == "4":
         division()

    if opcion == "5":
         salir()
         

main()

