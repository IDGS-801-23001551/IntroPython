'''
Crear un programa que tenga un menu con las siguientes opciones
'''
def suma():
     print("Seleccionaste suma")

def resta():
     print("Seleccionaste resta")

def multiplicacion():
     print("Seleccionaste multiplicacion")

def division():
     print("Seleccionaste division")

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

