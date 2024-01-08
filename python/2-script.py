#!/usr/bin/env python3

#Ejercicio 2: Crear una Clase Coche
#Crea una clase llamada Coche que tenga los atributos marca, modelo y año. Luego, 
#crea una instancia de la clase y muestra los valores de sus atributos.

class Coche:
    def __init__(self, marca=None, modelo=None, ano=None) -> None:
        if not marca or not isinstance(marca, str):
            raise ValueError('Debes ingresar una marca válida')
        
        if not modelo or not isinstance(modelo, str):
            raise ValueError('Debes ingresar un modelo válido')
        
        if not ano or not isinstance(ano, int):
            raise ValueError('Debes ingresar un año válido')

        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def __str__(self) -> str:
        return f'marca -> {self.marca}\nmodelo -> {self.modelo}\nano -> {self.ano}'

try:  
    # Instancia correctamente creada
    bmw = Coche("BMW", "ix2", 2024)
    print(bmw.__str__())
except ValueError as e:
    print(f'Ha ocurrido un error al crear el bmw: {e}')

try:  
    # Instancia incompleta
    bmw2 = Coche("ix2", 2024)
    print(bmw2.__str__())
except ValueError as e:
    print(f'Ha ocurrido un error al crear el bmw2: {e}')