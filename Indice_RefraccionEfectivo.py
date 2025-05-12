print("Inicializando entorno para cálculo de índice de refracción efectivo")

""" Importando librerias """
import numpy as np


""" Definiendo función para el cálculo del índice de refracción efectivo """

def indice_RefraccionEfectivo(angulo_Tetah, indice_RefraccionNucleo):

    #Cálculo de la variable recibe a "Tetah" en radianes.
    indice_refraccionEfectivo = indice_RefraccionNucleo*np.sin(angulo_Tetah)

    return indice_refraccionEfectivo

""" Definición de variables asociadas al problema de estudio """

# Índice de refracción del núcleo del guía de onda
n_nucleo = 1.5

# Ángulo tetah asociado al modo de estudio --> TALLER PARTE 01
tetah_modo0TE = 1.3095852
tetah_modo1TE = 1.0383224
tetah_modo2TE = 0.7655079
tetah_modo0TM = 1.2729923
tetah_modo1TM = 0.9699283
tetah_modo2TM = 0.7424246

# Se define variable en la cual se asignará el cálculo del índice de refracción efectivo
resultado_indiceRefraccionEfectivomodo0TE = indice_RefraccionEfectivo(tetah_modo0TE,n_nucleo)
resultado_indiceRefraccionEfectivomodo1TE = indice_RefraccionEfectivo(tetah_modo1TE,n_nucleo)
resultado_indiceRefraccionEfectivomodo2TE = indice_RefraccionEfectivo(tetah_modo2TE,n_nucleo)
resultado_indiceRefraccionEfectivomodo0TM = indice_RefraccionEfectivo(tetah_modo0TM,n_nucleo)
resultado_indiceRefraccionEfectivomodo1TM = indice_RefraccionEfectivo(tetah_modo1TM,n_nucleo)
resultado_indiceRefraccionEfectivomodo2TM = indice_RefraccionEfectivo(tetah_modo2TM,n_nucleo)


# Mostrando resultados en consola
print(resultado_indiceRefraccionEfectivomodo0TE)
print(resultado_indiceRefraccionEfectivomodo1TE)
print(resultado_indiceRefraccionEfectivomodo2TE)
print(resultado_indiceRefraccionEfectivomodo0TM)
print(resultado_indiceRefraccionEfectivomodo1TM)
print(resultado_indiceRefraccionEfectivomodo2TM)