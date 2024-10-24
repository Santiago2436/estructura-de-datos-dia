#Listas
#definicion de una lista
lista = [] #lista vacia
lista1 = ['Este es un texto'] #Una lista con un elemento
lista2 = ['Una cadena', 123] #Una lista de dos elementos
lista3 = [1, 2, 3, 4.5, 'hola', 'a'] #Una lista de seis elementos
print(lista)
print(lista1)
print(lista2)
print(lista3)

#listas enlazadas
lista5 = [0, 1, 2, 3]
lista6 = ("A","B","C")
lista7 = (lista5,lista6)
print(lista7[0])#Muestra solo lista5
print(lista7[1])#Muestra solo lista6
print(lista7[1][0])#Muestra de la lista6 el elemento de indice 0

#Operaciones con listas
#Concatenacion
lista8 = ["A","B","C","E"]
lista9 = [1,2,3,4,5]
lista10 = lista8 + lista9
print(lista10)
print(lista10[2])

#El metodo extend agrega una lista  al final de otra lista, la operacion afecta la litsa invcante
nombres1 = ["Antonio","Maria", "Mabel"]
nombres2 =["Barry","John","Guttag"]
#nombres3 =["Barry","John", "Guttag"]
print(nombres1)
print(nombres2)

#Operaciones con listas
#repetir
lista11 = [1,2,3,4,5]
lista12 = lista11*3
print(lista12)

#Comparacion
#Usando los operadores convencionakes (<, <=, >, >=, == !=)
print(["Rojas", 123]< ["Rosas", 123])
print(["Rosas", 123]== ["rosas", 123])
print(["Rosas", 123]> ["Rosas", 23])

#Operaciones con listas
#Es posible determianr si un elemento se encuentra en una lista
lista13 = ["cien", "años","de","soledad"]
if "de" in lista13:
    print("si esta en la lista")
else:
    print("No esta en la lista")

#Iterando una lista
lista15 = ["hola", "amigos","mios"]
for palabra in lista15: #para cada palabra de la litsa
    print(palabra, end=",")#parametro end evita salto de linea
