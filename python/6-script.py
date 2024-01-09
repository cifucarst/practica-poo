#!/usr/bin/env python3

# Ejercicio 6: Crear una Clase Libro
# Crea una clase llamada Libro que tenga los atributos título, autor y año_publicación. 
#Luego, crea un método dentro de la clase que muestre la información completa del 
#libro en formato "Título, Autor (Año de Publicación)".

class Libro:
    def __init__(self, titulo=None, autor=None, ano_publicacion=None):
        if titulo is None or not isinstance(titulo, str):
            raise ValueError("Debes ingresar un título válido")
        
        if autor is None or not isinstance(autor, str):
            raise ValueError("Debes ingresar un autor válido")
        
        if ano_publicacion is None or not isinstance(ano_publicacion, int):
            raise ValueError("Debes ingresar un año de publicación válido")
        
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacion = ano_publicacion

    def __str__(self):
        return f'{self.titulo}, {self.autor} ({self.ano_publicacion})'

try:
    primer_libro = Libro("Como ser un lammer", "Marcelo Vásquez", 2024)
    print(primer_libro)
except ValueError as e:
    print(f'Ha ocurrido un error en el primer libro: {e}')

try:
    segundo_libro = Libro("Como ser un lammer", "Marcelo Vásquez")
    print(segundo_libro)
except ValueError as e:
    print(f'Ha ocurrido un error en el segundo libro: {e}')