print("Inicializando entorno para cálculo de índice de refracción efectivo")

""" Importando librerias """
import numpy as np


""" Definiendo función para el cálculo del índice de refracción efectivo --> MÉTODO TRAZADO DE RAYOS"""

def indice_RefraccionEfectivoTrazadoRayos(angulo_Tetah, indice_RefraccionNucleo):

    #Cálculo de la variable recibe a "Tetah" en radianes.
    indice_refraccionEfectivo = indice_RefraccionNucleo*np.sin(angulo_Tetah)

    return indice_refraccionEfectivo

""" Definición de variables asociadas al problema de estudio """

# Índice de refracción del núcleo del guía de onda
n_nucleo = 1.5

# Índice de refracción del cladding del guía de onda
n_cladding = 1

#Longitud de onda 
longitud_onda = 1E-6 #Unidades en METROS [m]

#Ancho del núcleo del guía de onda
ancho_Nucleo = 1E-6 #Unidades en METROS [m]

#Velocidad de la luz
c = 3E8 #Unidades en METROS/SEGUNDO [m/s]

#Número de onda
numero_OndaVacio = 2*np.pi/longitud_onda

#Frecuencia angular
frecuencia_Angular = numero_OndaVacio*c

#Permeabilidad en el vacío
permeabilidad_vacio = (4E-7)*np.pi #Unidades H/m


""" Definiendo paŕametros de tetah"""

# Ángulo tetah asociado al modo de estudio --> TALLER PARTE 01
tetah_modo0TE = 1.3095852
tetah_modo1TE = 1.0383224
tetah_modo2TE = 0.7655079
tetah_modo0TM = 1.2729923
tetah_modo1TM = 0.9699283
tetah_modo2TM = 0.7424246

# Se define variable en la cual se asignará el cálculo del índice de refracción efectivo
resultado_indiceRefraccionEfectivomodo0TE = indice_RefraccionEfectivoTrazadoRayos(tetah_modo0TE,n_nucleo)
resultado_indiceRefraccionEfectivomodo1TE = indice_RefraccionEfectivoTrazadoRayos(tetah_modo1TE,n_nucleo)
resultado_indiceRefraccionEfectivomodo2TE = indice_RefraccionEfectivoTrazadoRayos(tetah_modo2TE,n_nucleo)
resultado_indiceRefraccionEfectivomodo0TM = indice_RefraccionEfectivoTrazadoRayos(tetah_modo0TM,n_nucleo)
resultado_indiceRefraccionEfectivomodo1TM = indice_RefraccionEfectivoTrazadoRayos(tetah_modo1TM,n_nucleo)
resultado_indiceRefraccionEfectivomodo2TM = indice_RefraccionEfectivoTrazadoRayos(tetah_modo2TM,n_nucleo)


# Mostrando resultados en consola
print("Trazado de rayos")
print(resultado_indiceRefraccionEfectivomodo0TE)
print(resultado_indiceRefraccionEfectivomodo1TE)
print(resultado_indiceRefraccionEfectivomodo2TE)
print(resultado_indiceRefraccionEfectivomodo0TM)
print(resultado_indiceRefraccionEfectivomodo1TM)
print(resultado_indiceRefraccionEfectivomodo2TM)


""" Calculando constantes de propagación Beta para cada uno de los modos """
beta_modo0TE = resultado_indiceRefraccionEfectivomodo0TE*numero_OndaVacio
beta_modo1TE = resultado_indiceRefraccionEfectivomodo1TE*numero_OndaVacio
beta_modo2TE = resultado_indiceRefraccionEfectivomodo2TE*numero_OndaVacio
beta_modo0TM = resultado_indiceRefraccionEfectivomodo0TM*numero_OndaVacio
beta_modo1TM = resultado_indiceRefraccionEfectivomodo1TM*numero_OndaVacio
beta_modo2TM = resultado_indiceRefraccionEfectivomodo2TM*numero_OndaVacio


""" Definiendo función para el cálculo del índice de refracción efectivo --> MÉTODO ANÁLISIS ONDULATORIO """
""" CONSIDERACIÓN --> En desarrollo método gráfico x = (kappa um)/2; y = (gamma um)/2"""


#Se define variable para clasificar caso según desarrollo con variable gamma o kappa
# --> 0 = Análisis con kappa
# Análisis con gamma en cualquier otro caso
caso = 0

def indice_RefraccionEfectivoOndulatorio(indice_RefraccionNucleo, indice_RefraccionCladding, coordenadaX,coordenadaY):

    if caso == 0:
        
        indice_refraccionEfectivo = np.sqrt((indice_RefraccionNucleo**2) - ((coordenadaX/np.pi)**2))

    else:

        indice_refraccionEfectivo = np.sqrt(((coordenadaY/np.pi)**2) + (indice_RefraccionCladding**2))

    return indice_refraccionEfectivo


""" Definición parámetros calculados para cada uno de los modos --> En caso de análisis ondulatorio """

# Coordenadas de interceptos --> TALLER PARTE 02
modo0TE = [1.2169799538,3.294839197]
modo1TE = [2.392320866,2.571321]
modo2TE = [3.3977765,0.890011778]
modo0TM = [1.38271479,3.2287932]
modo1TM = [2.66418983,2.2889076]
modo2TM = [3.472235987,0.52969938]


# Se define variable en la cual se asignará el cálculo del índice de refracción efectivo
resultado_indiceRefraccionEfectivomodo0TE = indice_RefraccionEfectivoOndulatorio(n_nucleo,n_cladding,modo0TE[0],modo0TE[1])
resultado_indiceRefraccionEfectivomodo1TE = indice_RefraccionEfectivoOndulatorio(n_nucleo,n_cladding,modo1TE[0],modo1TE[1])
resultado_indiceRefraccionEfectivomodo2TE = indice_RefraccionEfectivoOndulatorio(n_nucleo,n_cladding,modo2TE[0],modo2TE[1])
resultado_indiceRefraccionEfectivomodo0TM = indice_RefraccionEfectivoOndulatorio(n_nucleo,n_cladding,modo0TM[0],modo0TM[1])
resultado_indiceRefraccionEfectivomodo1TM = indice_RefraccionEfectivoOndulatorio(n_nucleo,n_cladding,modo1TM[0],modo1TM[1])
resultado_indiceRefraccionEfectivomodo2TM = indice_RefraccionEfectivoOndulatorio(n_nucleo,n_cladding,modo2TM[0],modo2TM[1])


# Mostrando resultados en consola
print("Análisis ondulatorio --> kappa")
print(resultado_indiceRefraccionEfectivomodo0TE)
print(resultado_indiceRefraccionEfectivomodo1TE)
print(resultado_indiceRefraccionEfectivomodo2TE)
print(resultado_indiceRefraccionEfectivomodo0TM)
print(resultado_indiceRefraccionEfectivomodo1TM)
print(resultado_indiceRefraccionEfectivomodo2TM)


# Se define variable en la cual se asignará el cálculo del índice de refracción efectivo

"""  MODIFICACIÓN DE CASO """
caso = 1

resultado_indiceRefraccionEfectivomodo0TE = indice_RefraccionEfectivoOndulatorio(n_nucleo,n_cladding,modo0TE[0],modo0TE[1])
resultado_indiceRefraccionEfectivomodo1TE = indice_RefraccionEfectivoOndulatorio(n_nucleo,n_cladding,modo1TE[0],modo1TE[1])
resultado_indiceRefraccionEfectivomodo2TE = indice_RefraccionEfectivoOndulatorio(n_nucleo,n_cladding,modo2TE[0],modo2TE[1])
resultado_indiceRefraccionEfectivomodo0TM = indice_RefraccionEfectivoOndulatorio(n_nucleo,n_cladding,modo0TM[0],modo0TM[1])
resultado_indiceRefraccionEfectivomodo1TM = indice_RefraccionEfectivoOndulatorio(n_nucleo,n_cladding,modo1TM[0],modo1TM[1])
resultado_indiceRefraccionEfectivomodo2TM = indice_RefraccionEfectivoOndulatorio(n_nucleo,n_cladding,modo2TM[0],modo2TM[1])


# Mostrando resultados en consola
print("Análisis ondulatorio --> gamma")

print(resultado_indiceRefraccionEfectivomodo0TE)
print(resultado_indiceRefraccionEfectivomodo1TE)
print(resultado_indiceRefraccionEfectivomodo2TE)
print(resultado_indiceRefraccionEfectivomodo0TM)
print(resultado_indiceRefraccionEfectivomodo1TM)
print(resultado_indiceRefraccionEfectivomodo2TM)


"""  Definiendo función para cálculo de contantes de NORMALIZACIÓN, en función de cada modo """

def constantes_Normalizacion(frecuencia_Angular,constante_propagacionBeta,ancho_nucleo,coordenadaY,coordenadaX,permeabilidad_Vacio):

    #Calculando constante c1 de normalización
    C1 = np.sqrt((4*frecuencia_Angular*permeabilidad_Vacio)/(constante_propagacionBeta*(ancho_nucleo + (1/coordenadaY))))

    #Calculando constante c0 de normalización
    C0 = C1 * np.cos(coordenadaX*ancho_nucleo)

    "Definiendo variable a la cual se le asignan las contantes de normalización calculadas "
    constantes_Normalizacion = [C0,C1]


    return constantes_Normalizacion



# Se define variable en la cual se asignará el cálculo de las constantes de propagación

constantes_NormalizacionModo0TE = constantes_Normalizacion(frecuencia_Angular,beta_modo0TE,ancho_Nucleo,modo0TE[1],modo0TE[0],
                                                           permeabilidad_vacio)
constantes_NormalizacionModo1TE = constantes_Normalizacion(frecuencia_Angular,beta_modo1TE,ancho_Nucleo,modo1TE[1],modo1TE[0],
                                                           permeabilidad_vacio)
constantes_NormalizacionModo2TE = constantes_Normalizacion(frecuencia_Angular,beta_modo2TE,ancho_Nucleo,modo2TE[1],modo2TE[0],
                                                           permeabilidad_vacio)
constantes_NormalizacionModo0TM = constantes_Normalizacion(frecuencia_Angular,beta_modo0TM,ancho_Nucleo,modo0TM[1],modo0TM[0],
                                                           permeabilidad_vacio)
constantes_NormalizacionModo1TM = constantes_Normalizacion(frecuencia_Angular,beta_modo1TM,ancho_Nucleo,modo1TM[1],modo1TM[0],
                                                           permeabilidad_vacio)
constantes_NormalizacionModo2TM = constantes_Normalizacion(frecuencia_Angular,beta_modo2TM,ancho_Nucleo,modo2TM[1],modo2TM[0],
                                                           permeabilidad_vacio)


# Mostrando resultados en consola
print(constantes_NormalizacionModo0TE)
print(constantes_NormalizacionModo1TE)
print(constantes_NormalizacionModo2TE)
print(constantes_NormalizacionModo0TM)
print(constantes_NormalizacionModo1TM)
print(constantes_NormalizacionModo2TM)

