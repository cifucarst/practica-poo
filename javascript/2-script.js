//Ejercicio 2: Métodos en una clase

// Extiende la clase Persona del ejercicio anterior para incluir un método llamado 
// saludar(), que mostrará un mensaje de saludo en la consola. Crea una instancia de la 
// clase y llama al método saludar().

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

    saludar(){
        console.log(`Buenos dias, mi nombre es ${this.nombre} y mi edad es ${this.edad} anos`)
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
nuevaPersona.saludar();