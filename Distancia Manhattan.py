def distancia_manhattan():
    """Distancia Manhattan"""
    
print("Programa para calcular la distancia Manhattan entre p1(x1, y1) y p2(x2, y2).")

# Se le solicita al usuario ingresar los datos de las coordenadas
print("Ingrese las coordenadas del p1:")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
p1 = (x1, y1)

print("Ingrese las coordenadas del p2:")
x2 = float(input("x2: "))
y2 = float(input("y2: "))
p2 = (x2, y2)

# Se calcula la distancia Manhattan con la siguiente fórmula: d = |x2 - x1| + |y2 - y1|
distancia_manhattan = abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
# Se agrega abs para el valor absoluto

# Se utiliza f-strings para un formato correcto en el resultado
print(f"\nLa distancia Manhattan entre {p1} y {p2} es: {distancia_manhattan:.2f}")
