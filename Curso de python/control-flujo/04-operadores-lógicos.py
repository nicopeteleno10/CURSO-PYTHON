# and, or, not

gas = True #ambos tienen que ser true para que nos imprima "puedes avanzar"
encendido = True
edad = 18

#Operadores de corto circuito significan que si el valor a la izquierda de and es falso, el de la derecha ya no se evalua, algo parecido pasa con or, si el de la izq es true, el de la derecha ya no se evalúa

if gas and encendido and edad > 17:
    print("Legal")
else:
    print("No")
#-------------------------------------------------

if not gas or encendido or edad > 17:
    print("Puedes avanzar")
else:
    print("NEVER")

#if gas or encendido:
    #print("Puedes avanzar")
#if gas and encendido:
    #print("Puedes Avanzar")
#if not gas or encendido:
    #print("Puedes Aavanzar")
    