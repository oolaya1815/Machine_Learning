# Contact with Python

We will proceed to implement a function in Python: def integrates_mc(fun, a, b, num_points) that will calculate the integral of a mathematical function bounded between a and b, to define its accuracy we will use the parameter num_points for its use in the Monte Carlo method.

The explanation of the Monte Carlo algorithm can be found in the following [link](https://en.wikipedia.org/wiki/Monte_Carlo_method)

Two algorithms have been realized, one using loops and the other using the numpy library.

## 1. Using for and while loops

File monte\_bucle.py

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

To generate a graph of the function and the random points, the following lines of code have been added to the previous function, and the function integra\_mc is evoked with the following arguments: fun = function, a = 0, b = 0.9, num\_points = 1000

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

Using the Python function scipy.integrate.quad, we will verify if the implemented function really gives a value close to the integral, we will also plot the error for different numbers of random points using the following code.

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

It can be seen that the greater the number of random points the error becomes small, there is a point that seems that the value on the x-axis is zero, but in reality it is 100 number of samples, compared to the scale gives that impression.

## 2. Using the Numpy library

File monte\_numpy.py

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

To generate a graph of the function and the random points, the following lines of code have been added to the previous function, and the function integra\_mc is evoked with the following arguments: fun = function, a = 0, b = 0.9, num\_points = 1000

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

Using the Python function scipy.integrate.quad, we will verify if the implemented function really gives a value close to the integral, we will also plot the error for different numbers of random points using the following code.

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

It can be seen that the greater the number of random points the error becomes small, there is a point that seems that the value on the x-axis is zero, but in reality it is 100 number of samples, compared to the scale gives that impression.

## 3. Comparison of execution times between the use of loops and the numpy library.

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

It can be seen that the time to execute the code that uses loops is much longer compared to the numpy library, the execution time of numpy appears to be very close to zero, but this is due to the big difference on the loop times, if we proceed to zoom in, the execution time of numpy is better appreciated

![fig6](https://github.com/oolaya1815/Machine_Learning/blob/main/Appendix/images/fig6.JPG)

The coded function is very useful to calculate the value of an integral in the first quadrant of the Cartesian axis, if the function is outside this quadrant the function fails and the necessary adjustments should be made, but for the objectives of this practice meets the requirements, since the functions with which the measurements have been made belong to the first quadrant, an example of this failure is seen in using the sine function in a range from 0 to 2.

![fig7](https://github.com/oolaya1815/Machine_Learning/blob/main/Appendix/images/fig7.JPG)

