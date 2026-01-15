''' Operacion de multiplicacion de a x b utilizando sumas
a=3
b=4

salida 3+3+3+3=12
'''

a=3
b=4
x=0

tem=""

while x<b:
    x+=1
    tem+=str(a)
    if x<b:
        tem+=("+")
    

Resultado = int(a*b)
tem+=str("=")+str(Resultado)
print(tem)