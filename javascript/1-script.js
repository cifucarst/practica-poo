/*Crea una clase llamada Persona que tenga dos propiedades: nombre y edad. Luego, crea una instancia de esta
clase y muestra sus propiedades en la consola*/

// Definición de la clase Persona
class Persona {
    // El constructor recibe un objeto con propiedades nombre y edad
    constructor({
        nombre,
        edad,
    }) {
        // Se valida que el nombre sea una cadena no vacía
        if (typeof nombre !== 'string' || nombre === '') {
            throw new Error('El nombre debe ser una cadena no vacía.');
        }
        
        // Se valida que la edad sea un número positivo
        if (typeof edad !== 'number' || edad < 0) {
            throw new Error('La edad debe ser un número positivo.');
        }

        // Se asignan las propiedades nombre y edad al objeto actual (this)
        this.nombre = nombre;
        this.edad = edad;
    }

    // Método para mostrar en la consola el nombre y la edad de la persona
    mostrar() {
        console.log(`${this.nombre} ${this.edad}`);
    }
}

// Crear una nueva instancia (objeto) de la clase Persona con nombre "Miguelito" y edad 36
const nuevaPersona = new Persona({
    nombre: "yenny",
    edad: 36
});

// Llamar al método mostrar de la instancia nuevaPersona para imprimir en la consola su nombre y edad
nuevaPersona.mostrar();