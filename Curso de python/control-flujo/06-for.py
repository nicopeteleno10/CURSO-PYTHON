for numero in range(5):#range5 nos devuelve una cadena de numeros hasta el 4 ( 5 - 1)
    print(numero) 
    #siguiente uso del for
buscar = 10
for numero in range(5):#iterable(cualquier cosa con la que podamos iterar)
    if numero == buscar:
        print("encontrado", buscar)
        break  #detener la ejecucion de nuestro codigo cuando encuentre el 3
else:
    print("no encontre el numero buscado")
    
#ejemplos de iterables

for char in "Ultimate python":
    print(char)
    
    