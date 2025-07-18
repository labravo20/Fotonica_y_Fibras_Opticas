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
archivo_entrada_X = "DELTA_nx_DATA.txt"
archivo_entrada_Y = "DELTA_ny_DATA.txt"

# Leer archivo X
col1_x, col2_x = read_data(folder, archivo_entrada_X)
guardar_columna(os.path.join(folder, "columna_1_x.txt"), col1_x)
guardar_columna(os.path.join(folder, "columna_2_x.txt"), col2_x)

# Leer archivo Y
col1_y, col2_y = read_data(folder, archivo_entrada_Y)
guardar_columna(os.path.join(folder, "columna_1_y.txt"), col1_y)
guardar_columna(os.path.join(folder, "columna_2_y.txt"), col2_y)

print("Todos los archivos han sido procesados y guardados correctamente.")

#Reemplazando los puntos por comas en todas las columnas --> Objetivo de procesamiento de datos en excel
reemplazar_puntos_por_comas(folder, "columna_1_x.txt")
reemplazar_puntos_por_comas(folder, "columna_2_x.txt")
reemplazar_puntos_por_comas(folder, "columna_1_y.txt")
reemplazar_puntos_por_comas(folder, "columna_2_y.txt")



# #Definiendo nombre de documentos asociados a graficación
# filename1 = 'DELTA_nx_DATA.txt'
# filename2 = 'DELTA_ny_DATA.txt'

# #Función para lectura de documento
# def read_data(folder, filename):
#     x_values = []
#     y_values = []
#     filepath = os.path.join(folder, filename)  # Crear la ruta completa al archivo
#     with open(filepath, 'r') as file:
#         for line in file:
#             parts = line.split()
#             if len(parts) >= 2:
#                 try:
#                     x = float(parts[0])
#                     y = float(parts[1])
#                     x_values.append(x)
#                     y_values.append(y)
#                 except ValueError:
#                     print(f"Advertencia: No se pudo convertir los valores en la línea: {line.strip()}")
#             else:
#                 print(f"Advertencia: Línea mal formateada o vacía: {line.strip()}")
#     return x_values, y_values



# Especificar la carpeta donde se encuentran los archivos
# folder = '/home/labravo/Desktop/Fotónica y fibras ópticas/Proyecto final' 
# # Leer los datos de los archivos
# x1_values, y1_values = read_data(folder, filename1)
# x2_values, y2_values = read_data(folder, filename2)



# fig, ax1 = plt.subplots()
# ax1.plot(x1_values, y1_values, marker='', color='r',linestyle='--', label='Δnx')
# ax1.set_xlabel('y (μm)')
# ax1.tick_params(axis='y', labelcolor='k')
# ax1.plot(x2_values, y2_values, marker='', color='k',label='Δny')
# ax1.legend(fontsize=12)
# ax1.set_ylim([4,16])
# ax1.set_xlim([50,100])
# ax1.legend()
# ax1.set_ylabel('Cambio en el índice de refracción (10^-3)')



# # Ajustar límites del eje y si es necesario
# #ax1.set_ylim([min(y1_values + y2_values + y3_values) * 0.456, max(y1_values + y2_values + y3_values) * 2.5])

# # Mejorar la visibilidad de las etiquetas
# ax1.tick_params(axis='x', which='major', labelsize=8)  # Tamaño de fuente para etiquetas mayores
# ax1.tick_params(axis='y', which='minor', labelsize=8)  # Tamaño de fuente para etiquetas menores
# fig.tight_layout()  # Ajusta mejor el espacio
# plt.show()