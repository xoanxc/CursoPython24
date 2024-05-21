# Introducción a Python

# Operaciones matemáticas básicas
print("Operaciones Matemáticas Básicas:")
a = 10
b = 5
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}\n")

# Manejo de listas
print("Manejo de Listas:")
fruits = ["manzana", "banana", "cereza"]
print("Lista de frutas:", fruits)
fruits.append("naranja")
print("Después de agregar naranja:", fruits)
fruits.remove("banana")
print("Después de quitar banana:", fruits)
print(f"La primera fruta en la lista es: {fruits[0]}\n")

# Control de flujo: condicionales y bucles
print("Control de Flujo:")
for fruit in fruits:
    if fruit == "cereza":
        print(f"Encontré una cereza!")
    else:
        print(f"{fruit} no es una cereza")

print()

# Definición de funciones
print("Funciones:")
def saludar(nombre):
    return f"Hola, {nombre}!"

print(saludar("Mundo"))
print(saludar("Pythonista"))

def suma(x, y):
    return x + y

print(f"La suma de 7 y 3 es: {suma(7, 3)}\n")

# Manejo de archivos
print("Manejo de Archivos:")
filename = "ejemplo.txt"
# Escribir en un archivo
with open(filename, "w") as file:
    file.write("Esto es un archivo de ejemplo.\n")
    file.write("Python es genial!\n")

# Leer desde un archivo
with open(filename, "r") as file:
    content = file.read()

print("Contenido del archivo:")
print(content)

# Manejo de excepciones
print("Manejo de Excepciones:")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("¡Error! No se puede dividir por cero.")

print("\nPrograma terminado.")
