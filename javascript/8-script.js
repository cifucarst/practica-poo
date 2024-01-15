// Ejercicio 7: Composición

// Crea una clase llamada Motor que tenga propiedades como potencia y tipo. Luego, 
// crea una clase Coche que tenga una propiedad motor que sea una instancia de la clase 
// Motor. Agrega métodos a la clase Coche para encender y apagar el motor.


class Motor {
    constructor({ potencia, tipo }) {
      this.potencia = potencia;
      this.tipo = tipo;
    }
  }
  
  class Coche {
    constructor({ motor }) {
      if (!(motor instanceof Motor)) {
        // Manejo de error: se espera que motor sea una instancia de la clase Motor
        throw new Error('El motor proporcionado no es válido.');
      }
  
      this.motor = motor;
      this.encendido = false;
    }
  
    encender() {
      if (!this.encendido) {
        this.encendido = true;
        console.log('El coche está encendido.');
      } else {
        throw new Error('El coche ya está encendido.');
      }
    }
  
    apagar() {
      if (this.encendido) {
        this.encendido = false;
        console.log('El coche está apagado.');
      } else {
        throw new Error('El coche ya está apagado.');
      }
    }
  }
  
  // Ejemplo de uso con manejo de errores
  try {
    const motorCoche = new Motor({
      potencia: "100w",
      tipo: "c"
    });
  
    const coche1 = new Coche({
      motor: motorCoche
    });
  
    coche1.encender();
    coche1.apagar();
    coche1.encender();
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }