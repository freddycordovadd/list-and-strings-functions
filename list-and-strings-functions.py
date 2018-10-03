"""
Funciones basicas de una lista de numeros
"""

# Lista de numeros
numeros=[100, 33, 16, 15, 16, 2, 99, 45, 16, 54]

# Imprimiendo el mayor de los numeros
print(str(max(numeros)))

# Agregando 112 a la lista
numeros.append(112)
print(numeros)

# Verificando nuevamente el mayor
print(str(max(numeros)))
print("-"*20)

# Conteo de un elemento / Todos los elementos
print(numeros.count(16))
print(len(numeros))

# Saber el indice de la primera coincidencia de un elemento
# Con index el elemento tiene q existir, sino error
print(numeros.index(16))

# Insertar en un indice en particular

numeros.insert(2, 25)
print(numeros)
print("-"*20)

# Hacer un pop con el ultimo obj de la lista
# Pop: Quitar el ultimo elemento y mostrarlo
print(numeros.pop())
print(numeros)

# Pop en indice particular

print(numeros.pop(2))
print(numeros)

# Reversa a la lista

numeros.reverse()
print(numeros)

# Ordenar la lista de menor a mayor y viceversa

numeros.sort()
print(numeros)
numeros.sort(reverse=True)
print(numeros)

# Promedio de los numeros
print(sum(numeros)/len(numeros))

# Crear nueva lista derivada de la lista numeros

lista2 = [(num * 100) for num in numeros]
print(lista2)

# Confirmar si un dato esta en la lista
print(100 in numeros)
print("Hola" in numeros)

print("======================================================")
print("========= Aqui termina la parte de listas =========")
print("======================================================")


"""
Funciones de cadenas de texto 'str' Ingresamos
un nombre y le hacemos modificaciones
"""
nombre = str(input("Ingresa el nombre: "))
print("-"*20)

# Mostrando el nombre
print(nombre)

# Mostrando el nombre a la inversa
print(nombre[::-1])

# string en mayusculas
print(nombre.upper())

# string en minusculas
print(nombre.lower())

# Capitalize string
print(nombre[:1].upper() + nombre[1:].lower())

# Mostrando el nombre con letras desordenadas
import random
print("".join(random.sample(nombre, len(nombre))))

# Mostrando largo de la cadena
print("El largo del texto es: " + str(len(nombre)))

# Separando cadena en caracteres
letras = []
for char in nombre:
    letras.append(char)

print(letras)
