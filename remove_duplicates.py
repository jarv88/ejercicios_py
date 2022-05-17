lista = [1,3,5,4,7,8,9,3,4,7,5,2,8,3,1,2,2]

new_list =[]

for i in range(len(lista)):
    if lista[i] not in new_list:
        new_list.append(lista[i])

print(new_list)


#otro forma con set

lista2 = [1,3,5,4,7,8,9,3,4,7,5,2,8,3,1,2,2]

new_list2 = set()

for i in range(len(lista2)):
    new_list2.add(lista2[i]) # list(new_list2) -> para convertir a array

print(new_list2)


#forma super rapida con set
lista3 = [1,3,5,4,7,8,9,3,4,7,5,2,8,3,1,2,2]

new_list3 = set(lista3)

new_list3 = list(new_list3) # para convertir a array
print(new_list3)

