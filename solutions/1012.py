A, B, C = map(float, input().split())
pi = 3.14159
# Calculating areas
triangle = (A * C) / 2
circle = pi * (C ** 2)
trapezium = ((A + B) * C) / 2
square = B ** 2
rectangle = A * B
print(f"TRIANGULO: {triangle:.3f}")
print(f"CIRCULO: {circle:.3f}")
print(f"TRAPEZIO: {trapezium:.3f}")
print(f"QUADRADO: {square:.3f}")
print(f"RETANGULO: {rectangle:.3f}")
