#Tuplas

tupla1 = () #tupla vacia
print(tupla1)
tupla2 = ('Esto es un texto',) #una tupla con un elemento que es una cadena
print(tupla2)
tupla3 = ('Una cadena', 123) #una tupla con dos elementos
print(tupla3)
tupla4 = ('apple', 2018, 'Samsung', 4.9, 't', True) #una tupla de seis elementos
print(tupla4)

tupla5 = (2, 4.7, 'Nota', 5, 3, 2.9)
print(tupla5[1])
print(tupla5[2])
print(tupla5[3])

tupla6 = (0, 1, 2, 3)
tupla7 = ('A', 'B', 'C')
tupla8 = (tupla6, tupla7)
print(tupla7)
print(tupla7[0]) #Muestra solo la tupla 1
print(tupla7[1]) #Muestra solo la tupla 2
print(tupla7[1][0]) #Muestra de la tupla 2 el elemento en el índice 0

#concatenar
tupla9 = ('A', 'B', 'C', 'E')
tupla10 = (1, 2, 3, 4, 5)
tupla11 =tupla9 + tupla10
print(tupla10)

#Repetir
#Crear una tupla con multiples copias de una tupla
tupla12 = (1, 2, 3, 4, 5)
tupla13 = tupla12 * 3
print(tupla13)

#Comparar
#Se usan los operadores convencionales (<, <=, >, >=, ==, !=)
tupla14 = ('Rojas',)
tupla15 = (123,)
tupla16 = ('Rosas',)
tupla17 = ('rosas',)
print((tupla14, tupla15) < (tupla16, tupla17))
print((tupla16, tupla15) == (tupla17, tupla15))

