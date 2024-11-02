print("Bienvenidos a la calculadora")
print("Para salir escribe salir")
print("Las operaciones son suma, resta, multi y div")

resultado = ""
while True:
    if not resultado:#este not me esta diciendo que el resultado es false, ya que el false es interpretado cuando hay unas comillas vacias, un "None" o un "False" o un 0
        resultado = input("Ingrese numero: ")#lo siguiente que vamos a hacer es validar si el usuario ha o no ha escrito salir
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)#si el usuario no escribio el string de salir convertimos el resultado en un numero entero
    op = input("Ingresa operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingrese el siguiente numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)#hacemos lo mismo que con el resultado
    
    if op.lower() == "suma":
        resultado += n2 
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2 
    else:
        print("Operacion no valida")
        break    
    #ahora ya le podemos mostrar el valor calculado al usuario
       
    print(f"El resultado es {resultado}")#la f hace que podamos incluir variables o expresiones dentro de una cadena de texto
    