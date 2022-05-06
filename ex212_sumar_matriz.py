# Sumar Filas y Columnas de una Matriz y Crear Matriz Resultante
new_el=0
matriz = [[25,69,51,26],
          [68,35,29,54],
          [54,57,45,63],
          [61,68,47,59]]
new_row=[]

for i, row in enumerate(matriz):
    for j, el in enumerate(row):
        new_el+=matriz[j][i]
    new_row.append(new_el)
    new_el=0

        #new_el+=matriz[index][0]
    #new_row.append(row[0])

matriz.append(new_row)
new_el=0

for index,row in enumerate(matriz):

    for el in row:
        new_el+=el

    row.append(new_el)
    new_el=0

for index,row in enumerate(matriz):
    print(row)

