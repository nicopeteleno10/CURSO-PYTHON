#numero = 1
#while numero < 100:
    #print(numero)
    #numero *= 2 #multiplica el numero 1 por 2


comando = ""

while True: #esto corre el programa de la misma forma que el comentario de abajo pero en un loop infinito (aunque pongas salir no sale del programa)
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir": #al ser un loop infinito, siempre escribir una condicion de salida
        break


#while comando.lower() != "salir":
    #comando = input("$ ")
    #print(comando)