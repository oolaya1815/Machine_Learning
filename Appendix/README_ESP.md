# Toma de contacto con Python

Se procedera a implementar una función en Python: def integra\_mc(fun, a, b, num\_puntos) que calculara la integral de una función matemática acotada entre a y b, para definir su exactitud se usar el parametro num\_puntos para su uso en el método de Monte Carlo.

La explicación del algoritmo de Monte Carlo se puede encontrar en el siguiente [link](https://es.wikipedia.org/wiki/M%C3%A9todo_de_Montecarlo)

Se ha realizado dos algoritmos uno usando bucles y otro mediante la biblioteca numpy.

## 1. Usando bucles for y while

Archivo monte\_bucle.py

```python
import random as rd
import matplotlib.pyplot as plt
import math

function = lambda x: -2*x**6-x**5+x**4-2*x**3+2*x+1

def integra_mc(fun, a, b, num_puntos):

	# inicializando las variables
	count = 0
	in_area = 0.0
	x_coord = []
	y_fun = []
	y_coord = []

	# Generando la cantidad de 'num_puntos' puntos aleatorios en el eje x en el
	# rango de a y b, cálculo del valor máximo de la función con los
	# puntos ya calculados
	for i in range(num_puntos):
		x = rd.uniform(a, b)
		x_coord.append(x)
		y_fun.append(function(x))
	maxy = max(y_fun)

	# Generando la cantidad de 'num_puntos' puntos aleatorios en el eje y, en el
	# rango de '0' y el máximo valor de la función también procedemos a contar
	# cuántos de estos puntos caen por debajo de la función

	while count < num_puntos:
		y_coord.append(rd.uniform(0, maxy))
		if y_coord[count] < y_fun[count]:
			in_area += 1
		count += 1

	# Cálculo del valor de la integral
	area_box = (b-a)*maxy
	I_monte = in_area*area_box/count
	return I_monte
```

Generamos un gráfico de la función y los puntos aleatorios, para realizarlo se ha procedido agregar las siguientes líneas código a la función anterior, y se evoca a la función integra\_mc con los siguientes argumentos:  fun = function, a =  0, b =  0.9, num\_puntos = 1000

```python
plt.figure(figsize=(10, 10))
plt.title(" $f(x)=-2x^6-x^5+x^4-2x^3+2x+1$ ", fontsize=14)
plt.xlabel('Coordena x', fontsize=14)
plt.ylabel('Coordena y', fontsize=14)
plt.plot(x_coord, y_fun, '.', c='red', linewidth=0.5, label='función')
plt.plot(x_coord, y_coord, 'x', c='blue', linewidth=0.5, label='aleatorios')
plt.legend(loc='upper left', prop={'size': 14}, frameon=True)
plt.show()
```
![fig1](https://github.com/oolaya1815/Machine_Learning/blob/main/Appendix/images/fig1.JPG)

Usando la función scipy.integrate.quad de Python, verificaremos si realmente la función implementada da un valor cercano a la integral, también se graficara el error para distinto números de puntos aleatorios usando el siguiente código.

```python
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
	plt.title("Uso de bucles", fontsize=14)
	plt.xlabel('Número de puntos aleatorios', fontsize=14)
	plt.ylabel('Valor del error', fontsize=14)
	plt.plot(sizes, error, 'x', c='blue', linewidth=0.5, label='error')
	plt.plot(sizes, linea, c='red')
	plt.legend(loc='upper right', prop={'size': 20}, frameon=True)
	plt.show()
```

![fig2](https://github.com/oolaya1815/Machine_Learning/blob/main/Appendix/images/fig2.JPG)

Se aprecia que a un mayor número de puntos aleatorios el error se hace pequeño, existe un punto que pareciera que el valor en el eje x es cero, pero en realidad es de 100 número de muestras, comparado con la escala da  esa impresión.

## 2. Uso de la librería Numpy

Archivo monte\_numpy.py

```python
import numpy as np
import matplotlib.pyplot as plt 

def function(x): return -2*x**6-x**5+x**4-2*x**3+2*x+1

def integra_mc(fun, a, b, num_puntos):
    # inicializando variables
    in_area = 0.0
    
    # generando la cantidad de ‘num_puntos’ puntos aleatorios en el eje x en el
    # rango de a y b, y cálculo del valor máximo de la función con los 
    # puntos ya calculados
    x_coord = np.random.uniform(a, b, num_puntos)
    y_fun = function(x_coord)
    maxy = np.amax(y_fun)

    # generando la cantidad de ‘num_puntos’ puntos aleatorios en el eje y en el
    # rango de ‘0’ y el máximo valor de la función también procedemos a contar
    # cuántos de estos puntos caen por debajo de la de la función
    y_coord = np.random.uniform(0, maxy, num_puntos)
    mask = (y_coord < y_fun)
    in_area = len(y_coord[mask])

    # cálculo del valor de la integral
    area_box = (b-a)*maxy
    I_monte = in_area*area_box/num_puntos
    return I_monte
```

Generamos un gráfico de la función y los puntos aleatorios, para realizarlo se ha procedido agregar las siguientes líneas código a la función anterior, y se evoca a la función integra_mc con los siguientes argumentos:  fun = function, a =  0, b =  0.9, num_puntos = 1000

```python
plt.figure(figsize=(10, 10))
plt.title(" $f(x)=-2x^6-x^5+x^4-2x^3+2x+1$ ", fontsize=14)
plt.xlabel('coordenada x', fontsize=14)
plt.ylabel('coordenada y', fontsize=14)
plt.plot(x_coord, y_fun, '.', c='red', linewidth=0.5, label='función')
plt.plot(x_coord, y_coord, 'x', c='blue', linewidth=0.5, label='aleatorios')
plt.legend(loc='upper left', prop={'size': 14}, frameon=True)
plt.savefig('montecarlo_bucle.png')
plt.show()
```

![fig3](https://github.com/oolaya1815/Machine_Learning/blob/main/Appendix/images/fig3.JPG)

Usando la función scipy.integrate.quad de Python, verificaremos si realmente la función implementada da un valor cercano a la integral, también se graficara el error para distintos números de puntos aleatorios usando el siguiente código.

```python
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
```

![fig4](https://github.com/oolaya1815/Machine_Learning/blob/main/Appendix/images/fig4.JPG)

Se aprecia que a un mayor número de puntos aleatorios el error se hace pequeño, existe un punto que pareciera que el valor en el eje x es cero, pero en realidad es de 100 número de muestras, comparado con la escala da  esa impresión.

## 3. Comparación de los tiempos de ejecución entre el uso de bucles y la biblioteca numpy

```python
import time
import numpy as np
import matplotlib.pyplot as plt
import random as rd

function = lambda x: -2*x**6-x**5+x**4-2*x**3+2*x+1

def integra_mc_bucle(fun, a, b, num_puntos):
    """Calcula la integral con bucles
    y devuelve el tiempo en milisegundos"""
    tic = time.process_time()
    count = 0
    in_area = 0.0
    x_coord = []
    y_fun = []
    y_coord = []

    for i in range(num_puntos):
        x = rd.uniform(a, b)
        x_coord.append(x)
        y_fun.append(function(x))
    
    maxy = max(y_fun)

    while count < num_puntos:
        y_coord.append(rd.uniform(0, maxy))
        if y_coord[count] < y_fun[count]:
            in_area += 1
        count += 1

    area_box = (b-a)*maxy
    I = in_area*area_box/count
    toc = time.process_time()
    return 1000 * (toc-tic)

def integra_mc_numpy(fun, a, b, num_puntos):
    """Calcula la integral con librería numpy
    y devuelve el tiempo en milisegundos"""
    tic = time.process_time()
    in_area = 0.0
    x_coord = np.random.uniform(a, b, num_puntos)
    y_fun = function(x_coord)
    maxy = np.amax(y_fun)
    y_coord = np.random.uniform(0, maxy, num_puntos)
    mask = (y_coord < y_fun)
    in_area = len(y_coord[mask])
    area_box = (b-a)*maxy
    I = in_area*area_box/num_puntos
    toc = time.process_time()
    return 1000 * (toc-tic)

def compara_timepos():
    sizes = np.linspace(100, 100000, 20)
    times_dot = []
    times_fast = []
    for size in sizes:
        times_dot += [integra_mc_bucle(function, 0, 0.9, int(size))]
        times_fast += [integra_mc_numpy(function, 0, 0.9, int(size))]
    
    plt.style.use('seaborn-whitegrid')
    plt.figure(figsize=(10,10))
    plt.title("Comparación de los tiempos de ejecución", fontsize=14)
    plt.xlabel('Número de puntos', fontsize=14)
    plt.ylabel('Tiempo de ejecución en ms', fontsize=14)
    plt.scatter(sizes, times_dot, c='red', label='bucle')
    plt.scatter(sizes, times_fast, c='blue', label='numpy')
    plt.legend(loc='upper left', prop={'size': 14}, frameon=True)
    plt.savefig('tiempo.png')

compara_timepos()
```

![fig5](https://github.com/oolaya1815/Machine_Learning/blob/main/Appendix/images/fig5.JPG)

Se aprecia que los tiempos para ejecutar el código que usa bucles es mucho mayor comparado con la librería numpy, el tiempo de ejecución de numpy aparenta estar muy cerca a cero, pero esto se debe a la gran diferencia sobre los tiempos del bucle, si procedemos hacer un zoom, se aprecia mejor el tiempo de ejecución de numpy

![fig6](https://github.com/oolaya1815/Machine_Learning/blob/main/Appendix/images/fig6.JPG)

La función codificada es muy útil para calcular el valor de una integral en el primer cuadrante del eje cartesiano, si la función se encuentra fuera de este cuadrante la función falla y se debería realizar los ajuste necesarios, pero para los objetivos de esta práctica cumple los requerimientos, ya que las funciones con que se han realizado las mediciones pertenecen al primer cuadrante, un ejemplo de esta falla se aprecia en usar la función seno en un rango de 0 a 2.

![fig7](https://github.com/oolaya1815/Machine_Learning/blob/main/Appendix/images/fig7.JPG)
