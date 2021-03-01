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

