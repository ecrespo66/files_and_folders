from files_and_folders.files import File

# Crear una instancia de la clase File usando la ruta de un archivo
archivo = File("testdata/readme.md")

# Mostrar información básica del archivo
print(f"Ruta: {archivo.path}")
print(f"Existe: {archivo.exists}")
print(f"Nombre del archivo: {archivo.file_name}")
print(f"Tamaño (en bytes): {archivo.byte_size}")
print(f"Fecha de creación: {archivo.creation_datetime}")
print(f"Última fecha de modificación: {archivo.modification_datetime}")

# Renombrar el archivo
archivo.rename("nuevo_nombre.md")

# Hacer una copia del archivo en una nueva ubicación
archivo.copy("testdata/subfolder/copia_nuevo_nombre.txt")

# Mover el archivo a una nueva ubicación
archivo.move("testdata/subfolder/")

# Esperar hasta que el archivo exista (útil para la sincronización)
archivo.wait_for_file_to_exist(timeout=15)

# Eliminar el archivo (usar con precaución)
#archivo.remove()

