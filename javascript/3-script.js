//Ejercicio 3: Herencia

//Crea una clase llamada Estudiante que herede de la clase Persona. La clase Estudiante
//debe tener una propiedad adicional llamada curso. Crea una instancia de la clase 
//Estudiante y muestra todas sus propiedades en la consola

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

    saludar() {
        console.log(`Buenos días, mi nombre es ${this.nombre} y mi edad es ${this.edad} años y soy una persona`);
    }

    // Método para mostrar en la consola el nombre y la edad de la persona
    mostrar() {
        console.log(`${this.nombre} ${this.edad}`);
    }
}

class Estudiante extends Persona {
    constructor({
        nombre,
        edad,
        curso,
    }) {
        // Se llama al constructor de la clase padre (Persona) con nombre y edad
        super({ nombre, edad });
        this.curso = curso;
    }

    saludar() {
        console.log(`Buenos días, mi nombre es ${this.nombre} y mi edad es ${this.edad} años, además soy una estudiante que está cursando ${this.curso}`);
    }
}

// Crear una nueva instancia (objeto) de la clase Estudiante con nombre "Yenny", edad 36 y curso "Programación"
const nuevoEstudiante = new Estudiante({
    nombre: "Yenny",
    edad: 36,
    curso: "Programación"
});

// Llamar al método mostrar de la instancia nuevoEstudiante para imprimir en la consola su nombre y edad
nuevoEstudiante.mostrar();

// Llamar al método saludar de la instancia nuevoEstudiante para imprimir en la consola un saludo personalizado
nuevoEstudiante.saludar();