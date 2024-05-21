# Listas
semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

print(semana[0])  # 'lunes'

print(semana[0:5])  # ['lunes', 'martes', 'miércoles', 'jueves', 'viernes']
print(semana[:5])  # ['lunes', 'martes', 'miércoles', 'jueves', 'viernes']

finde = semana[5:]
print(finde)  # ['sábado', 'domingo']

print(len(finde))  # 2

finde.append("lunes")
print(finde)  # ['sábado', 'domingo', 'lunes']

print(semana)  # ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']

for dia in semana:
    print(dia)

for indice in range(7):
    if indice % 2 == 1:
        print(semana[indice])

# Tuplas
tupla = ("lunes", "martes")

print(tupla[0])  # 'lunes'

precios = [
    ("manzanas", 2),
    ("naranjas", 3)
]

print(precios)  # [('manzanas', 2), ('naranjas', 3)]

print(precios[0])  # ('manzanas', 2)
print(precios[0][0])  # 'manzanas'
print(precios[1])  # ('naranjas', 3)

producto, precio = precios[0]
print(producto)  # 'manzanas'
print(precio)  # 2

# Instalación de Pillow (comentado para evitar ejecución en cada script)
# !pip install pillow

from PIL import Image

# Abre y muestra la imagen
perroIm = Image.open("perro.jpg")
perroIm.show()
