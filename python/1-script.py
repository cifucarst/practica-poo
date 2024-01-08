#Ejercicio 1: Crear una Clase Persona
#Crea una clase llamada Persona que tenga los atributos nombre y edad. Luego, crea una 
#instancia de la clase y muestra los valores de sus atributos.

# Definición de la clase Persona
class Persona:
    # Método constructor para inicializar una instancia de Persona
    def __init__(self, nombre=None, edad=None):
        # Verifica si el nombre no es válido (vacío o no es una cadena)
        if not nombre or not isinstance(nombre, str):
            # Levanta una excepción ValueError con un mensaje descriptivo
            raise ValueError('Debes ingresar un nombre válido')

        # Verifica si la edad no es válida (vacía o no es un entero)
        if not edad or not isinstance(edad, int):
            # Levanta una excepción ValueError con un mensaje descriptivo
            raise ValueError('Debes ingresar una edad válida')

        # Asigna los valores recibidos a los atributos de la instancia
        self.nombre = nombre
        self.edad = edad

    # Método especial para representar el objeto como una cadena
    def __str__(self):
        return f'Mi nombre es {self.nombre} y tengo {self.edad} años.'

# Intento crear una persona con los datos proporcionados
try:
    persona1 = Persona("Juan", 50)
    print(persona1.__str__())  # Imprime los datos de persona1
except ValueError as e:
    print(f"Error al crear persona1: {e}")  # Captura y muestra errores al crear persona1

# Intento crear otra persona con datos incompletos
try:
    persona2 = Persona("Alberto")
    print(persona2.__str__())  # Imprime los datos de persona2
except ValueError as e:
    print(f"Error al crear persona2: {e}")  # Captura y muestra errores al crear persona2

# Intento crear otra persona con datos inválidos (nombre vacío y edad como cadena)
try:
    persona3 = Persona("", "34")
    print(persona3.__str__())  # Imprime los datos de persona3 (no se llega aquí por los errores)
except ValueError as e:
    print(f"Error al crear persona3: {e}")  # Captura y muestra errores al crear persona3
