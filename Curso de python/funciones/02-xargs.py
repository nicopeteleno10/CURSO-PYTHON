def suma(*numeros):#este asterisco transforma los parametros en iterables #esto se hace para sumar todos los numeros que le pasamos a la funcion sin necesidad de escribirlos en el parametro print
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)#cuidado con la identacion, este print debe colocarse donde esta ahora, de otra forma, el programa nos mostraria el resultado mas veces de la debida



suma(2, 5, 7)
suma(2, 5, 7, 14, 29)

