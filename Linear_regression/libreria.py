import time
import numpy as np
from pandas.io.parsers import read_csv
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

def carga_csv(file_name):
    """ carga el fichero csv especificado y lo
        devuelve en un array de numpy """
    valores = read_csv(file_name, header=None).values
    # suponemos que siempre trabajaremos con float
    return valores.astype(float)

def normalizar(X):
    # numero de columnas, sin contar la columna de 1s
    n = np.shape(X[:, 1:])[1]
    Xn = X.copy() # copio la X
    Xmedia = [0]*n
    Xstd = [0]*n
    # va realizar la normalizacion de todas las columnas sin tomar
    # la columana del los 1s
    for i in range(n): 
        Xn[:, i+1] = (X[:, i+1]-X[:, i+1].mean())/X[:, i+1].std()
        Xmedia[i] = X[:, i+1].mean()
        Xstd[i] = X[:, i+1].std()
    return Xn, Xmedia, Xstd

def analiticatheta(X,Y):
    B = np.linalg.pinv(X.T @ X) @ X.T @ Y
    return B

def generadorXY(datos):
    X = datos[:, :-1]
    np.shape(X)         # (97, 1)
    Y = datos[:, -1]
    np.shape(Y)         # (97,)
    m = np.shape(X)[0]
    # añadimos una columna de 1's a la X
    X = np.hstack([np.ones([m, 1]), X])
    return X, Y

def coste(X, Y, Theta):
    # almacena en H todos los puntos de 
    # Theta[0] + X*Theta[1]
    H = np.dot(X, Theta) # hipotesis
    # vectorizacion
    Aux = (H - Y).T @ (H - Y)
    # se retorna el valor del producto escalar
    # divido entre dos veces el numero de elementos
    return Aux / (2 * len(X))

def gradiente(X, Y, Theta, alpha):
    # se alamacena la Theta inicial para su uso en el calculo
    # de la gradiente en un punto aleatorio de la funcion de coste
    NuevaTheta = Theta
    m = np.shape(X)[0]
    n = np.shape(X)[1]
    # almacena en H todos los puntos de
    # Theta[0] + X*Theta[1]
    H = np.dot(X, Theta)
    # almacena en Aux la diferencia de H e Y 
    Aux = (H - Y)
    # se recorre toda el arreglo de X y se le multiplica por Aux
    for i in range(n):
        Aux_i = Aux.T @ X[:, i]
        # al finalizar el bucle se queda con el ultimo valor
        # acumulado que seria el valor negativo de la gradiente
        # en el punto donde se llama a la funcion
        NuevaTheta[i] -= (alpha / m) * Aux_i
    return NuevaTheta

def descenso_gradiente(X, Y, t0_range, t1_range, alpha, iteraciones):
    # se define las variables para almacenar el coste y el historico
    # de theta
    costes = []
    thetahis = []
    # generamos un primer Theta en una poscion aleatoria
    # en el rango de t0_range y t1_range
    Theta = [np.random.uniform(t0_range[0], t0_range[1]),
             np.random.uniform(t1_range[0], t1_range[1])]
    for i in range(iteraciones):
        # se llama a la funcion gradiente, el primer Theta
        # es el calculado de forma aleatorio
        Theta = gradiente(X, Y, Theta, alpha)
        # para cada teta calculado se genera su coste
        costes.append(coste(X, Y, Theta)) # lita.append(valor)
        # se almacenara un numero de Thetas historicos
        if(i % 300 == 0):
            thetahis.append(Theta.copy())
    return Theta, costes, thetahis

def descenso_gradientemv(X, Y, alpha, iteraciones):
    # se define las variables para almacenar el coste y el historico
    # de theta
    costes = []
    Theta = [0]*np.shape(X)[1]
    for _ in range(iteraciones):
        # se llama a la funcion gradiente, el primer Theta
        # es el calculado de forma aleatorio
        Theta = gradiente(X, Y, Theta, alpha)
        # para cada teta calculado se genera su coste
        costes.append(coste(X, Y, Theta))  
    return Theta, costes

def make_data(t0_range, t1_range, X, Y):
    """Genera las matrices X,Y,Z para generar un plot en 3D"""
    step = 0.1
    Theta0 = np.arange(t0_range[0], t0_range[1], step)
    Theta1 = np.arange(t1_range[0], t1_range[1], step)
    Theta0, Theta1 = np.meshgrid(Theta0, Theta1)
    # Theta0 y Theta1 tienen las misma dimensiones, de forma que
    # cogiendo un elemento de cada uno se generan las coordenadas x,y
    # de todos los puntos de la rejilla
    Coste = np.empty_like(Theta0)
    for ix, iy in np.ndindex(Theta0.shape):
        Coste[ix, iy] = coste(X, Y, [Theta0[ix, iy], Theta1[ix, iy]])
    return [Theta0, Theta1, Coste]

def geninforme(X, Y, Theta, costes, thetahis, iteraciones, t0_range, t1_range):

    # generando los puntos necesarios para las graficas
    Theta0, Theta1, Coste = make_data(t0_range, t1_range, X, Y)
    # variables necesarias para el grafico
    sizes = np.linspace(0, iteraciones, iteraciones)
    H = np.dot(X, Theta)
    p0 = [thetahis[i][0] for i in range(len(thetahis))]
    p1 = [thetahis[i][1] for i in range(len(thetahis))]
    # se procede a generar los graficos para una mejor guia
    plt.style.use('seaborn-whitegrid')
    fig = plt.figure(figsize=(15, 15))

    # grafico de la regresión lineal
    plt.subplot(223)
    plt.title('Regresión lineal de los datos ex1data1.csv', fontsize=10)
    plt.xlabel('Población de la ciudad en 10.000s', fontsize=9)
    plt.ylabel('Ingresos en $10.000s', fontsize=9)
    plt.scatter(X[:, 1], Y, alpha=0.3,
                label='Ingresos vs Población')
    plt.plot(X[:, 1], H, color='r',
             label=str('{0:.2f}'.format(Theta[0])) +
             '+'+str('{0:.2f}'.format(Theta[1]))+'X')
    plt.legend(loc='upper left', prop={'size': 7}, frameon=True)

    # grafico del coste vs iteraciones
    plt.subplot(222)
    plt.title('Comportamiento del coste vs iteraciones', fontsize=10)
    plt.plot(sizes, costes)
    plt.xlabel('Iteraciones', fontsize=9)
    plt.ylabel('Valor del coste', fontsize=9)

    # grafico en 3d
    plt.subplot(224)
    ax = fig.add_subplot(2, 2, 4, projection='3d')
    plt.title('grafico de coste en 3d', fontsize=10)
    surf = ax.plot_surface(Theta0, Theta1, Coste, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    fig.colorbar(surf, shrink=0.5, aspect=5)

    # grafico de la función del coste vs Theta
    plt.subplot(221)
    plt.title('Función de coste y movimiento del theta', fontsize=10)
    plt.contour(Theta0, Theta1, Coste,
                np.logspace(-2, 3, 20), colors='blue')
    plt.plot(Theta[0], Theta[1], "x", c="red", label='mínimo: ' +
             '$\\theta_{0}$ = '+str('{0:.2f}'.format(Theta[0])) +
             ' y '+'$\\theta_{1}$='+str('{0: .2f}'.format(Theta[1])))
    plt.plot(p0, p1, "x", c="green", label='movimiento de $\\theta$')
    plt.xlabel('$\\theta_{0}$', fontsize=9)
    plt.ylabel('$\\theta_{1}$', fontsize=9)
    plt.legend(loc='upper left', prop={'size': 6}, frameon=True)
    plt.savefig('Practica1/Imagenes/informe'+str(time.time())+'.jpg', dpi=350)
    plt.show()
    return None