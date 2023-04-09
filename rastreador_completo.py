import os

# Nombre de los directorios donde buscar
ruta_busqueda = ["D:\\", "C:\\"]

# Nombre de los archivos y carpetas a bucar
informacion = ["datos", ".txt"]

# creamos el archivo que va a guardar las rutas
with open("informacion_direccion.txt", "w") as direccion_archivos:
    for ruta in ruta_busqueda:
        for root, dirs, files in os.walk(ruta):
            for valor in informacion:
                if valor in files:
                    # Archivo encontrado
                    direccion = os.path.join(root, valor)
                    direccion_archivos.write(direccion + "\n")
                elif valor in dirs:
                    # Carpeta encontrada
                    direccion = os.path.join(root, valor)
                    direccion_archivos.write(direccion + "\n")
