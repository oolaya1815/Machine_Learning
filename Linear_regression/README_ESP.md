# Regresión Lineal

En el repositorio se encuentre el archivo libreria.py que contiene todas las funciones que se han usado.

## 1. Regresión lineal con una variable


Se tiene los datos que encontrar los parámetros ø con lo que se  en base a la poblacióon de una ciudad, se va aplicar el método de descenso de gradiente en Python para encontrar los parámetros ø con lo que se defina una recta que se ajusta mejor a los datos de entrenamiento.

Los datos se procederán a importar del archivo ex1data1.csv con la ayuda de la siguiente función:

```python
def carga_csv(file_name):
    """ carga el fichero csv especificado y lo
    devuelve en un array de numpy"""
    valores = read_csv(file_name, header=None).values
    # suponemos que siempre trabajamos con datos en formato
    # float
    return valores.astype(float)

h<sub>&theta;</sub>(x) = &theta;<sub>o</sub> x + &theta;<sub>1</sub>x
