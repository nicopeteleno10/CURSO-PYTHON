saludo = "Hola global"#esta funcion tiene alcance global


def saludar():
    saludo = "Hola Mundo"#esta funcion solo tiene alcance en saludar
    print(saludo)#recordar siempre definir una variable antes y luego llamarla
    
    
def saludaChanchito():
    saludo = "Hola Chanchito"#esta funcion solo tiene alcance en saludaChanchito
    print(saludo)
    
#no podemos llamar a saludo fuera de la funcion saludar o saludochanchito, tenemos que hacerlo dentro
    
saludar()
print(saludo)


#no utilizar variables globales (recomendacion)
#si vamos a utilizar variables globales se hace de la siguiente forma:
def saludar():
    global saludo#ahora python ya sabe que esta variable de saludo es la que aparece en la primera linea
    saludo = "Hola Mundo"
