#!/usr/bin/env python3

#Ejercicio 7: Crear una Clase Empleado
#Crea una clase llamada Empleado que tenga los atributos nombre, puesto y salario. 
#Luego, crea un método dentro de la clase que incremente el salario de un empleado 
#en un porcentaje dado. Crea una instancia de la clase, aplique el aumento de salario 
#y muestra el nuevo salario.

class Empleado:
    def __init__(self, nombre=None, puesto=None, salario=None):
        if nombre is not None and not isinstance(nombre, str):
            raise ValueError("Debes ingresar un nombre válido")
        
        if puesto is not None and not isinstance(puesto, str):
            raise ValueError("Debes ingresar un puesto válido")
        
        if salario is not None and not isinstance(salario, (int, float)):
            raise ValueError("Debes ingresar un salario válido")
        
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

    def incrementar_salario(self, incremento):
        if not isinstance(incremento, (int, float)) or incremento <= 0:
            raise ValueError('Debes ingresar un incremento válido')
        
        # Se actualiza el salario utilizando la fórmula correcta para el aumento porcentual
        self.salario += self.salario * (incremento / 100)
        return self.salario

try:
    empleado1 = Empleado("Alberto", "manager", 100)
    print(empleado1.incrementar_salario(25))  # Aumenta el salario en un 25%
except ValueError as e:
    print(f'Ha ocurrido un error: {e}')

try:
    empleado2 = Empleado("manager", 100)
    print(empleado2.incrementar_salario(25))  # Aumenta el salario en un 25%
except ValueError as e:
    print(f'Ha ocurrido un error: {e}')