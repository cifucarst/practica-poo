//Ejercicio 6: Herencia y Polimorfismo

//Crea una clase base llamada Vehiculo con propiedades como marca, modelo, año, y 
//métodos como acelerar(), frenar(). Luego, crea clases derivadas como Coche y Moto 
//que hereden de Vehiculo y agreguen propiedades y métodos específicos para cada uno. 
//Ejecuta acciones como acelerar y frenar en instancias de ambas clases y muestra los 
//resultados.

class Vehiculo {
    constructor(marca, modelo, año) {
      this.marca = marca;
      this.modelo = modelo;
      this.año = año;
    }
  
    acelerar() {
      console.log(`El vehículo acelera`);
    }
  
    frenar() {
      console.log(`El vehículo frena`);
    }
}

  
class Coche extends Vehiculo {
    constructor(marca, modelo, año, potencia, asientos) {
      super(marca, modelo, año);
      this.potencia = potencia;
      this.asientos = asientos;
    }
  
    encender() {
      console.log(`El coche se enciende`);
    }
  
    apagar() {
      console.log(`El coche se apaga`);
    }
}


class Moto extends Vehiculo {
    constructor(marca, modelo, año, cilindrada, tipo) {
      super(marca, modelo, año);
      this.cilindrada = cilindrada;
      this.tipo = tipo;
    }

    hacerWheelie() {
      console.log(`La moto hace un wheelie`);
    }

    hacerBurnout() {
      console.log(`La moto hace un burnout`);
    }
}


const coche = new Coche("Ford", "Mustang", 2023, 200, 5);
coche.acelerar();
coche.frenar();
coche.encender();
coche.apagar();

const moto = new Moto("Honda", "CBR1000RR", 2022, 1000, "deportiva");
moto.acelerar();
moto.frenar();
moto.hacerWheelie();
moto.hacerBurnout();