#!/usr/bin/env python3

# Ejercicio 1: Clase Película
# Crea una clase llamada Pelicula que tenga los atributos titulo, director, año y duración.
# Implementa un método para mostrar la información completa de la película y otro método 
# que calcule la edad de la película (restando el año de lanzamiento al año actual).

from datetime import datetime

class Pelicula:
    def __init__(self, titulo, director, ano_lanzamiento, duracion) -> None:
        self.titulo = titulo
        self.director = director
        self.ano_lanzamiento = ano_lanzamiento
        self.duracion = duracion

    def __str__(self) -> str:
        return f'El título de la película es "{self.titulo}" dirigida por "{self.director}" del año {self.ano_lanzamiento} y tiene una duración de {self.duracion} minutos.'

    def edad_pelicula(self):
        fecha_actual = datetime.now()
        ano_actual = fecha_actual.year
        edad_actual_pelicula = ano_actual - self.ano_lanzamiento
        return f'La edad de la película es {edad_actual_pelicula} años.'

# Crear una instancia de la clase Pelicula
pelicula1 = Pelicula("Rápidos y Furiosos", "Carlos", 2020, 230)

# Imprimir información de la película y su edad
print(pelicula1.__str__())
print(pelicula1.edad_pelicula())