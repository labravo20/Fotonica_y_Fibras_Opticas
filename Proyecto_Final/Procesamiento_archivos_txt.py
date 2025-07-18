# Inicializando entorno de programación #
print("Hellou...")

#Importando librerias
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LogLocator, LogFormatter
from scipy.interpolate import splrep, splev
import os


#Función para lectura de data en doc tipo txt
def read_data(folder, filename):
    col1 = []
    col2 = []
    filepath = os.path.join(folder, filename)
    
    with open(filepath, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 2:
                try:
                    val1 = float(parts[0])
                    val2 = float(parts[1])
                    col1.append(val1)
                    col2.append(val2)
                except ValueError:
                    print(f"Advertencia: No se pudo convertir valores en la línea: {line.strip()}")
            else:
                print(f"Advertencia: Línea mal formateada o vacía: {line.strip()}")
    
    return col1, col2

#Función para guardar una columna de datos en un documento txt
def guardar_columna(ruta_salida, datos):
    with open(ruta_salida, 'w') as f:
        for valor in datos:
            f.write(f"{valor}\n")

#Función para reemplazar los puntos por comas en documento txt
def reemplazar_puntos_por_comas(folder, filename, nuevo_nombre=None):
    """
    Reemplaza todos los puntos por comas en un archivo .txt y guarda el resultado en otro archivo.
    
    Parámetros:
    - folder: carpeta donde está el archivo
    - filename: nombre del archivo original (ej. 'columna_1_x.txt')
    - nuevo_nombre: nombre del archivo de salida (opcional)
    """
    ruta_entrada = os.path.join(folder, filename)

    # Si no se especifica un nuevo nombre, agrega _comas al original
    if nuevo_nombre is None:
        nombre_base, extension = os.path.splitext(filename)
        nuevo_nombre = f"{nombre_base}_comas{extension}"

    ruta_salida = os.path.join(folder, nuevo_nombre)

    with open(ruta_entrada, 'r') as entrada, open(ruta_salida, 'w') as salida:
        for linea in entrada:
            salida.write(linea.replace('.', ','))

    print(f"Archivo convertido y guardado como: {ruta_salida}")


# Ruta donde están los archivos (ajústala según tu necesidad)
folder = "/home/labravo/Desktop/Fotónica y fibras ópticas/Proyecto final"

# Nombres de los archivos de entrada
archivo_entrada_X = "DELTA_nx.txt"
archivo_entrada_Y = "DELTA_ny.txt"

# Leer archivo X
col1_x, col2_x = read_data(folder, archivo_entrada_X)
guardar_columna(os.path.join(folder, "columna_1_x_barridoY.txt"), col1_x)
guardar_columna(os.path.join(folder, "columna_2_x_barridoY.txt"), col2_x)

# Leer archivo Y
col1_y, col2_y = read_data(folder, archivo_entrada_Y)
guardar_columna(os.path.join(folder, "columna_1_y_barridoY.txt"), col1_y)
guardar_columna(os.path.join(folder, "columna_2_y_barridoY.txt"), col2_y)

print("Todos los archivos han sido procesados y guardados correctamente.")

#Reemplazando los puntos por comas en todas las columnas --> Objetivo de procesamiento de datos en excel
reemplazar_puntos_por_comas(folder, "columna_1_x_barridoY.txt")
reemplazar_puntos_por_comas(folder, "columna_2_x_barridoY.txt")
reemplazar_puntos_por_comas(folder, "columna_1_y_barridoY.txt")
reemplazar_puntos_por_comas(folder, "columna_2_y_barridoY.txt")


