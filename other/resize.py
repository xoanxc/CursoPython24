# Ruta de la imagen original
ruta_imagen_original = "imagen_original.jpg"
# Ruta para guardar la imagen redimensionada
ruta_imagen_redimensionada = "imagen_redimensionada.jpg"

# Abrir la imagen original
imagen = Image.open(ruta_imagen_original)

# Mostrar información de la imagen original
print(f"Tamaño original: {imagen.size}")

# Definir el nuevo tamaño
nuevo_ancho = 800
nuevo_alto = 600

# Redimensionar la imagen
imagen_redimensionada = imagen.resize((nuevo_ancho, nuevo_alto))

# Mostrar información de la imagen redimensionada
print(f"Nuevo tamaño: {imagen_redimensionada.size}")

# Guardar la imagen redimensionada
imagen_redimensionada.save(ruta_imagen_redimensionada)

print("Imagen redimensionada guardada con éxito.")
