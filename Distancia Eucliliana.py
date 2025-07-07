print("Programa para calcular la distancia Eucliliana")
#Distancia Eucliliana
#Formula: d=√(x2 - x1)2 + (y2 - y1)2
import numpy as np #para obtener la raiz cuadrada
#se le solicita al usuario ingresar los valores de las coordenadas
print("Ingrese las coordenadas de x1 y y1 del p1")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
p1 = (x1, y1)

print("Ingrese las coordenadas de x2 y y2 para el p2")
x2 = float(input("x2: "))
y2 = float(input("y2: "))
p2 = (x2, y2)
# calcula la distancia eucliliana
distancia= (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

eucliliana_dist = np.sqrt(distancia)
print("El resultado de la distancia es:", eucliliana_dist)

