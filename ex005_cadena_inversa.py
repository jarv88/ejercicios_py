#Obtener representacion inversa de una cadena de caracteres

cadena = 'Python'
reverse=''
for i in range(len(cadena)-1,-1,-1):
    reverse+=cadena[i]
    print(cadena[i],end='') #end -> evitar salto de linea

#usando slycing

print(cadena[::-1])