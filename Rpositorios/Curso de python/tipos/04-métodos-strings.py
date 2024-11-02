animal = " chanCHito feliz "
print(animal.upper())#upper() es un metodo para que python imprima o reconozca la variable animal como todo en mayúsculas.
print(animal.lower())
print(animal.capitalize())#primera letra mayuscula, el primer caracter, al ser un espacio no lo pone en mayusculas
print(animal.title())#primera letra de cada palabra
print(animal.strip())#remueve todos los espacios
print(animal.strip().capitalize())#Esto elimina los espacios y pone la primera en mayusculas
print(animal.lstrip())#Espacios en blanco a la izquierda eliminados, lo mismo pasa con rstrip().
print(animal.rstrip())#lo mismo pasa con rstrip(), elimina los de la derecha
print(animal.find("CH"))#Busca una cadena de caracteres y nos devuelve el índice,es decir, donde se encuentra esa cadena, si devuelve -1, significa que no encontró la cadena
print(animal.replace("nCH", "j"))#reemplaza caracteres
print("nCH" in animal)#Esto nos devuelve un boolean, a diferencia de .find()
print("nCH" not in animal)



