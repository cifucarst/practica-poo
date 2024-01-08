#!/usr/bin/env python3

#Ejercicio 3: Crear una Clase Rectángulo
#Crea una clase llamada Rectangulo que tenga los atributos largo y ancho. Luego, 
#crea un método dentro de la clase que calcule el área del rectángulo. Crea una 
#instancia de la clase y muestra el área del rectángulo.

class Rectangulo:
    def __init__(self, largo, ancho) -> None:
        if not isinstance(largo, (int, float)) or not isinstance(ancho, (int, float)):
            raise ValueError('Los valores de largo y ancho deben ser números')

        if largo <= 0 or ancho <= 0:
            raise ValueError('Los valores de largo y ancho deben ser mayores que cero')

        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho

# instancia correcta
try:
    rect1 = Rectangulo(4, 6)
    print(f'El área del rectángulo es -> {rect1.area()}')
except ValueError as e:
    print(f'Error al crear el rectángulo: {e}')

print()

# instancia para probar manejo de errores
try:
    rect2 = Rectangulo(-4, 6)
    print(f'El área del rectángulo2 es -> {rect2.area()}')
except ValueError as e:
    print(f'Error al crear el rectángulo2: {e}')

print()

# instancia para probar manejo de errores
try:
    rect3 = Rectangulo("4", 6)
    print(f'El área del rectángulo3 es -> {rect3.area()}')
except ValueError as e:
    print(f'Error al crear el rectángulo3: {e}')