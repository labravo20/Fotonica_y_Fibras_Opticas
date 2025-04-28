""" Mensaje para verificar inicialización del proyecto """
print("Inicializando proyecto Newton-Brewster")

""" Importando librerias """
import numpy as np
from scipy.optimize import newton
import matplotlib.pyplot as plt


""" ################# INICIO Definición de funciones a estudiar ################## """

""" Funciones para estudio de ondas tipo TE """

# Definición de la función f(x) asociada a modos de ondas TE
def funcion_modosTE(x, m):
    term1 = 3 * np.pi * np.cos(x)
    term2 = 2 * np.arctan(((1 / (1.5 * np.cos(x))) * np.sqrt(2.25 * np.sin(x)**2 - 1)))
    return term1 - term2 - m * np.pi

# Derivada de la función f(x) de TE --> Resultado necesario para el Método de Newton-Brester
def funcion_modosTEDerivada(x, m):

    # Derivada de term1: 3*pi*cos(x)
    term1_prime = -3 * np.pi * np.sin(x)  

    # Derivada de term2: 2 * atan( (1 / (1.5 * cos(x))) * sqrt(2.25 * sin(x)^2 - 1) )
    term2_prime = 2 * (1 / (1 + ((1 / (1.5 * np.cos(x))) * np.sqrt(2.25 * np.sin(x)**2 - 1))**2)) * \
                  ((-1 / (1.5 * np.cos(x))) * np.sqrt(2.25 * np.sin(x)**2 - 1)) * \
                  np.cos(x)
    
    return term1_prime - term2_prime


""" Funciones para estudio de ondas tipo TE """

# Definición de la función f(x) asociada a modos de ondas TM
def funcion_modosTM(x, m):
    term1 = 3 * np.pi * np.cos(x)
    term2 = 2 * np.arctan((1.5 / np.cos(x)) * np.sqrt(2.25 * np.sin(x)**2 - 1))
    return term1 - term2 - m * np.pi

# Derivada de la función f(x) de TM --> Resultado necesario para el Método de Newton-Brester
def funcion_modosTMDerivada(x, m):
    
    # Derivada de term1: 3*pi*cos(x)
    term1_prime = -3 * np.pi * np.sin(x)  
    
    # Derivada de term2: 2 * atan( (1.5 / cos(x)) * sqrt(2.25 * sin(x)^2 - 1) )
    term2_prime = 2 * (1 / (1 + ((1.5 / np.cos(x)) * np.sqrt(2.25 * np.sin(x)**2 - 1))**2)) * \
                  ((-1.5 * np.sin(x)) * np.sqrt(2.25 * np.sin(x)**2 - 1)) * np.cos(x)
    
    return term1_prime - term2_prime


""" ################# FIN Definición de funciones a estudiar ################## """



""" Definición de función para implementación de método Newton-Brewster """

# Función para implementar Método de Newton-Brewster
def newton_brewster(f, f_prime, x0, m, tol=1e-6, max_iter=100):
    
    # Definición de condición inicial
    x = x0

    # Se establece un ciclo for para ejecutar las iteraciones necesarias
    for i in range(max_iter):
        fx = f(x, m)
        fpx = f_prime(x, m)

        # Se establece criterio de convergencia
        if abs(fx) < tol: 
            return x
        
        #Aplicando ecuación de Newton
        x = x - fx / fpx  

    # Se establece caso DEFAULT cuando resultado NO CONVERGE
    raise ValueError("No convergió después de {} iteraciones".format(max_iter))



""" Definición de condiciones iniciales """

# Valor inicial de x
x0 = 1.3

# Modo a evaluar en la función
m = 1   



"""Llamando función para encontrar raiz (si existe) teniendo en cuenta el modo 'm' predeterminado"""

# Llamando función para evaluar modos de ondas tipo TE
root = newton_brewster(funcion_modosTE, funcion_modosTEDerivada, x0, m)

# Llamando función para evaluar modos de ondas tipo TM
#root = newton_brewster(funcion_modosTM, funcion_modosTMDerivada, x0, m)


# Proyección de los resultados en consola
print(f"Raíz encontrada para m = {m}: x = {root}")

