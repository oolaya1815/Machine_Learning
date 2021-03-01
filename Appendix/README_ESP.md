# Toma de contacto con Python

Se procedera a implementar una funci�n en Python: def integra\_mc(fun, a, b, num\_puntos) que calculara la integral de una funci�n matem�tica acotada entre a y b, para definir su exactitud se usar el parametro num\_puntos para su uso en el m�todo de Monte Carlo.

La explicaci�n del algoritmo de Monte Carlo se puede encontrar en el siguiente [link](https://es.wikipedia.org/wiki/M%C3%A9todo_de_Montecarlo)

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
	# rango de a y b, c�lculo del valor m�ximo de la funci�n con los
	# puntos ya calculados
	for i in range(num_puntos):
		x = rd.uniform(a, b)
		x_coord.append(x)
		y_fun.append(function(x))
	maxy = max(y_fun)

	# Generando la cantidad de 'num_puntos' puntos aleatorios en el eje y, en el
	# rango de '0' y el m�ximo valor de la funci�n tambi�n procedemos a contar
	# cu�ntos de estos puntos caen por debajo de la funci�n

	while count < num_puntos:
		y_coord.append(rd.uniform(0, maxy))
		if y_coord[count] < y_fun[count]:
			in_area += 1
		count += 1

	# C�lculo del valor de la integral
	area_box = (b-a)*maxy
	I_monte = in_area*area_box/count
	return I_monte
```
