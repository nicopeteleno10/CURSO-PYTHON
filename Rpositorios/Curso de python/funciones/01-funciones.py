def hola(nombre, apellido="Feliz"):#la variable nombre solo se puede utilizar dentro de la funcion, para colocar varios parametros, se separan por coma
    print("Hola mundo!")
    print(f"Bienvenido {nombre} {apellido}")#cuando nos referimos a nombre en este print estamos haciendo referencia a un parametro de la funcion, no a la funcion en si misma
#el parametro es el nombre de la variable dentro de la funcion
#el valor que le estamos pasando

hola("Nicolas" , "Garcia")#este hola lo que hace es llamar a la funcion, ya que si no lo ponemos el archivo se ejecutara pero no imprimira nada
hola("Chanchito") #chanchito feliz o nicolas es un argumento

#Si definimos el parametro apellido en esa misma linea (linea 1), al haber dos llamamientos a la funcion, python va a corresponder el parametro "feliz" al llamamiento que solo tiene un argumento
#es decir, va a corresponder el parametro feliz como apellido de chanchito a "Chanchito" y no al de Nicolas garcia ya que ese ya tiene un argumento asignado




#de esta forma definimos cual de los dos va primero, definiendo cual es nombre y cual es apellido
hola(apellido="Garcia", nombre="Nicolas")