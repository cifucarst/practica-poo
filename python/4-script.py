#Ejercicio 4: Crear una Clase Cuenta Bancaria
#Crea una clase llamada CuentaBancaria que tenga los atributos saldo y titular. 
#Luego, crea métodos para depositar y retirar dinero de la cuenta. Asegúrate de 
#manejar casos en los que el retiro sea mayor que el saldo disponible.

class CuentaBancaria:
    SALDO_MAXIMO = 1000000

    def __init__(self, saldo, titular):
        if saldo <= 0:
            raise ValueError('El saldo debe ser mayor que 0.')
        self.saldo = saldo
        self.titular = titular

    def _validar_cantidad(self, cantidad):
        if not isinstance(cantidad, (int, float)):
            raise ValueError('Debes ingresar un número.')

    def retirar_dinero(self, cantidad):
        self._validar_cantidad(cantidad)
        if cantidad > self.saldo:
            return 'Debes ingresar una cantidad menor o igual a tu saldo actual.'
        elif cantidad <= 0:
            return 'Debes ingresar una cantidad positiva.'
        else:
            self.saldo -= cantidad
            return self.saldo

    def ahorrar_dinero(self, cantidad):
        self._validar_cantidad(cantidad)
        if cantidad < 0:
            raise ValueError('Debes ingresar una cantidad positiva o igual a 0.')
        elif cantidad + self.saldo > self.SALDO_MAXIMO:
            return f'No puedes ahorrar más de {self.SALDO_MAXIMO - self.saldo}.'
        else:
            self.saldo += cantidad
            return self.saldo

    @property
    def saldo_maximo(self):
        return self.SALDO_MAXIMO


# Ejemplo de uso
jhon = CuentaBancaria(500, "John")

print(jhon.retirar_dinero(-200))
print(jhon.retirar_dinero("200"))
print(jhon.retirar_dinero(100))

print(jhon.ahorrar_dinero(200))
print(jhon.ahorrar_dinero(10000000))
print(jhon.ahorrar_dinero("dae/"))
print(jhon.ahorrar_dinero(-200))