n1 = input("Ingresa primer numero")#input es la manera de comunicarnos con el usuario
n2 = input("Ingresa segundo numero")

n1 = int(n1)#para que sume los dos numeros y no los concatene, es decir, si le damos 12 y 10, nos devuelve 22 gracias al int, no 1210
n2 = int(n2)#ademas, int pasa de un string a un integer.

#definimos las operaciones
suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f""""
para los numeros{n1} y {n2}.
el resultado de la suma es {suma}.
el resultado de la resta es {resta}.
el resultado de la multiplicación es {multi}.
el resultado de la division es {div}.

"""
print(mensaje)