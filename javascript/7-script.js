// Ejercicio 6: Encapsulamiento y Métodos Estáticos

// Crea una clase llamada Banco que tenga una propiedad estática llamada tasaDeInteres 
// y métodos estáticos para calcular el interés. Luego, crea una clase CuentaBancaria 
// que tenga propiedades como saldo y titular y métodos para depositar y retirar dinero.
// Utiliza la tasa de interés del banco para calcular el interés ganado en una cuenta.


// Clase Banco
class Banco {
    // Propiedad estática para la tasa de interés
    static tasaDeInteres = 0.05; // Ejemplo: tasa de interés del 5%
  
    // Método estático para calcular el interés
    static calcularInteres(monto) {
      return monto * this.tasaDeInteres;
    }
  }
  
// Clase CuentaBancaria
class CuentaBancaria {
    constructor(titular, saldo) {
      this.titular = titular;
      this.saldo = saldo;
    }
  
    // Método para depositar dinero
    depositar(cantidad) {
      try {
        this.saldo += cantidad;
        console.log(`${this.titular}, has depositado ${cantidad} y tu nuevo saldo es ${this.saldo}`);
      } catch (error) {
        console.log(error);
      }
    }
  
    // Método para retirar dinero
    retirar(cantidad) {
      try {
        if (cantidad <= this.saldo) {
          this.saldo -= cantidad;
          console.log(`${this.titular}, has retirado ${cantidad} y tu nuevo saldo es ${this.saldo}`);
        } else {
          throw new Error(`Saldo insuficiente para retirar ${cantidad}`);
        }
      } catch (error) {
        console.log(error);
      }
    }
  
    // Método para calcular el interés usando la tasa de interés del Banco
    calcularInteres() {
      const interes = Banco.calcularInteres(this.saldo);
      console.log(`${this.titular}, el interés ganado es ${interes}`);
    }
  }
  
  // Ejemplo de uso
  const miBanco = new Banco();
  const cuenta1 = new CuentaBancaria("Juan", 1000);
  
  // Acceder a la tasa de interés del Banco
  console.log(`Tasa de interés del banco: ${Banco.tasaDeInteres}`);
  
  // Hacer un depósito
  cuenta1.depositar(500);
  
  // Retirar dinero
  cuenta1.retirar(200);
  
  // Calcular el interés ganado en la cuenta
  cuenta1.calcularInteres();