# Obtener un conjunto de numeros separados por coma y crear una lista


numeros = input("Ingrese lista de numeros: ")

lista_numeros=numeros.replace(' ', '').split(',',maxsplit=3)
print(lista_numeros)