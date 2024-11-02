#keyword args
def get_product(**datos):#con los kwargs se ponen 2 asteriscos
    print(datos["id"], datos["name"])#para especificar a que valor queremos acceder ponemos entre corchetes el nombre del valor
    
get_product(id="23",
            name="Iphone",
            desc="Esto es un iphone")