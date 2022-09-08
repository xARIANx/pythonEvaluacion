# 1 - recibir codigo nombre y precio
# 2 - digitar 1 para mostrar todos los productos y editar el precio 
# 3 - digitar 3 para permitir buscar por codigo un porducto y editar precio de este
# 4 - digitar 4 para permitir buscar por codigo un producto y eliminar el producto
# 5 - 0 cerrar 
lista = []
cont = 1
n = 1
cont = 1
while(n != 0):
    dicionari = {}
    n = int(input("digitar opcion"))
    if(n == 1):
       dicionari["codigo"] = int(input("digitar codigo"))
       dicionari["nombre"] = input("digitar nombre")
       dicionari["precio"] = int(input("digitar precio"))
       lista.append(dicionari)
    if(n == 2):
         print(f"tus datos ingresado fueron : {lista}") 
    if(n == 3):
        buscador = int(input("digitar codigo producto"))
        for e in lista:
            if(e["codigo"] == buscador): 
                modificacion = int(input("digitar nuevo precio"))
                e["precio"] = modificacion
                break
    if(n== 4 ):
        buscador = int(input("digitar codigo producto"))
        for e in lista:
            if(e["codigo"] == buscador):
                lista.remove(e)
                print("Product eleminado")
        