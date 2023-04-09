# Rastreador de Archivos
Se ha implementado un script en python que se encarga de buscar archivos y carpetas con informacion privada, tu defines los nombres a buscar en la computadora vulnerada, este script te devolvera la ruta donde encuntra dichos archivos y carpetas.

### Requisitos 
- Python 
- vitualenv
------------------------------------------

## Ejecucion del Archivo

- Clonamos el archivo 
```python
git clone 
```
> Tu puedes modificar los nombres de los archivos y carpetas, segun sea tu necesidad de busqueda

- Ejecucion del script basico
```python
python rastreador_basico.py
```

- Ejecucion del script completo
```python
python rastreador_completo.py
```


## Creacion de Nuestro Entorno de Trabajo (Opcional)
---------------------------------

- Creamos el entorno virtual
```python
python -m virtualenv venv
```

- Ejecutamos virtualenv
```python
.\venv\Scripts\activate
```

- Detemos virtualenv
```python
deactivate
```


- Instalacion de Librerias para Convertir de .py a .exe


```python
pip install zstandard Nuitka ordered-set
```

- Comando para Convertir de .py a .exe

```
py -m nuitka --mingw64 --onefile "nombreArchivo.py"
```
