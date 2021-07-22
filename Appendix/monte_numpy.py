#grafica y generación de puntos aleatorios con numpy  

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def function(x): return -2*x**6-x**5+x**4-2*x**3+2*x+1

def integra_mc(fun, a, b, num_puntos):

    in_area = 0.0
    x_coord = np.random.uniform(a, b, num_puntos)
    y_fun = function(x_coord)
    maxy = np.amax(y_fun)
    y_coord = np.random.uniform(0, maxy, num_puntos)
    mask = (y_coord < y_fun)
    in_area = len(y_coord[mask])
    area_box = (b-a)*maxy
    I_monte = in_area*area_box/num_puntos

    plt.style.use('seaborn-whitegrid')
    plt.figure(figsize=(10, 10))
    plt.title(" $f(x)=-2x^6-x^5+x^4-2x^3+2x+1$ ", fontsize=14)
    plt.xlabel('coordenada x', fontsize=14)
    plt.ylabel('coordenada y', fontsize=14)
    plt.plot(x_coord, y_fun, '.', c='red', linewidth=0.5, label='función')
    plt.plot(x_coord, y_coord, 'x', c='blue', linewidth=0.5, label='aleatorios')
    plt.legend(loc='upper left', prop={'size': 14}, frameon=True)
    plt.show()

    return I_monte


def compara_error():

    sizes = np.linspace(100, 100000, 20)
    error = []
    linea = []
    I = integrate.quad(function, 0, 0.9)
    for size in sizes:
        error += [integra_mc(function, 0, 0.9, int(size)) - I[0]]
        linea += [0]
    plt.style.use('seaborn-whitegrid')
    plt.figure(figsize=(10, 10))
    plt.title("Librería numpy", fontsize=14)
    plt.xlabel('Número de puntos aleatorios', fontsize=14)
    plt.ylabel('Valor del error', fontsize=14)
    plt.plot(sizes, error, 'x', c='blue', linewidth=0.5, label='error')
    plt.plot(sizes, linea, c='red')
    plt.legend(loc='upper right', prop={'size': 20}, frameon=True)
    plt.show()

integra_mc(function, 0, 0.9, 1000)
compara_error()
