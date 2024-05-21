# Operaciones básicas
print(2 + 3 * 6)  # 20

potencia = 2**10
print(potencia)  # 1024

print(10 / 3)  # 3.3333333333333335

print(10 // 3)  # División entera: 3
print(10 % 3)  # Resto: 1

# Tipos de datos
a = 5
a = "Hola"
print(type(a), type(5))  # (str, int)

# Entrada y salida
print("Hola")
print("¿Cómo te llamas?")
nombre = input()
print("Encantado de conocerte " + nombre)

print(nombre.isnumeric())  # False

# Condicionales
if 3 > 4:
    print("5 es mayor que 4")
else:
    print("No se cumple")

# Programa que pida la edad y determine si eres mayor o menor de edad
print("Inserta la edad:")
edad = input()
if edad.isnumeric():
    edad = int(edad)
    if edad >= 18:
        print("Mayor de edad")
    else:
        print("Menor de edad")
else:
    print("Debes escribir un número")

# Bucle while para pedir la edad hasta que se ingrese un número válido
while True:
    print("Inserta la edad:")
    edad = input()
    if edad.isnumeric():
        edad = int(edad)
        if edad >= 18:
            print("Mayor de edad")
        else:
            print("Menor de edad")
        break
    else:
        print("Debes escribir un número")

# Trabajando con listas
valores = [4, 5, 3, 8, 2, 7, 9]
print(valores[0])  # 4

for valor in valores:
    print(valor)

print(type(valores))  # list
print(type(valor))  # int

# Instalación de matplotlib (comentado para evitar ejecución en cada script)
# !pip install matplotlib

import matplotlib.pyplot as grafica

x = range(len(valores))
print(list(x))  # [0, 1, 2, 3, 4, 5, 6]

grafica.bar(x, valores)
grafica.show()  # Descomentar para mostrar el gráfico de barras

grafica.boxplot(valores)
grafica.show()  # Descomentar para mostrar el boxplot
