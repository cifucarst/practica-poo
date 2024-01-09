#!/usr/bin/env python3

#Ejercicio 5: Crear una Clase Estudiante
#Crea una clase llamada Estudiante que tenga los atributos nombre, edad y nota. Luego, 
#crea un método dentro de la clase que determine si el estudiante ha aprobado 
#(nota mayor o igual a 5) o ha reprobado (nota menor a 5). Crea una instancia de la 
#clase y muestra si el estudiante ha aprobado o reprobado.

class Estudiante:
    def __init__(self, nombre=None, edad=None, nota=None) -> None:
        if not nombre or not isinstance(nombre, str):
            raise ValueError('Debes ingresar un nombre válido')

        if edad is not None and (not isinstance(edad, int) or edad <= 0):
            raise ValueError('Debes ingresar una edad válida')
        
        if not nota and (not isinstance(nota, (int,float)) or nota < 0):
            raise ValueError('Debes ingresar una nota valida')

        self.nombre = nombre
        self.edad = edad
        self.nota = nota

    def aprobar_o_reprobar(self):
        return self.nota >= 5

    def __str__(self) -> str:
        return f'El estudiante {self.nombre} ha aprobado el curso -> {self.aprobar_o_reprobar()}'

try:
    alumno1 = Estudiante("Daniel", 22,5)
    print(alumno1.__str__())
except ValueError as e:
    print(f'Error ocurrido en alumno1: {e}')

try:
    alumno2 = Estudiante("Alberto", 22,-5)
    print(alumno2.__str__())
except ValueError as e:
    print(f'Error ocurrido en alumno2: {e}')