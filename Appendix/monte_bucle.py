#grafica y generación de puntos aleatorios con bucles

import random as rd
import matplotlib.pyplot as plt
import math


def function(x): return math.sin(x)

def integra_mc(fun, a, b, num_puntos):

    # inicializando las variables
    count = 0
    in_area = 0.0
    x_coord = []
    y_fun = []
    y_coord = []

    # generando la cantidad de ‘num_puntos’ puntos aleatorios en el eje x en el
    # rango de a y b, con y cálculo del valor máximo de la función con los
    # puntos ya calculados
    for i in range(num_puntos):
        x = rd.uniform(a, b)
        x_coord.append(x)
        y_fun.append(function(x))
    maxy = max(y_fun)

    # generando la cantidad de ‘num_puntos’ puntos aleatorios en el eje y en el
    # rango de ‘0’ y el máximo valor de la función también procedemos a contar
    # cuántos de estos puntos caen por debajo de la de la función

    while count < num_puntos:
        y_coord.append(rd.uniform(0, maxy))
        if y_coord[count] < y_fun[count]:
            in_area += 1
        count += 1

    # cálculo del valor de la integral
    area_box = (b-a)*maxy
    I_monte = in_area*area_box/count

    plt.style.use('seaborn-whitegrid')
    plt.figure(figsize=(10, 10))
    plt.title(" $f(x)=sin(x)$ ", fontsize=14)
    plt.xlabel('Coordena x', fontsize=14)
    plt.ylabel('Coordena y', fontsize=14)
    plt.plot(x_coord, y_fun, '.', c='red', linewidth=0.5, label='función')
    plt.plot(x_coord, y_coord, 'x', c='blue', linewidth=0.5, label='aleatorios')
    plt.annotate('área no calculada', xy=(4.8, -0.5),  xycoords='data',
                 xytext=(0.5, 0.2), textcoords='axes fraction',
                 arrowprops=dict(facecolor='black', shrink=0.05),
                 horizontalalignment='right', verticalalignment='top')
    plt.legend(loc='upper left', prop={'size': 14}, frameon=True)
    plt.show()
    print(I_monte)
    return I_monte

integra_mc(function, 0, 2*math.pi, 1000)
