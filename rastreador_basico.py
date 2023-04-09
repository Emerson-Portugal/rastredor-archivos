import os

ruta_busqueda = "D:\\"

informacion = ["datos", "amigos.txt"]

with open("informacion_direccion.txt", "w") as direccion_archivos:
    for root, dirs, files in os.walk(ruta_busqueda):
        for valor in informacion:
            if valor in files:
                direccion = os.path.join(root, valor)
                direccion_archivos.write(direccion + "\n")

            elif valor in dirs:
                direccion = os.path.join(root, valor)
                direccion_archivos.write(direccion + "\n")
